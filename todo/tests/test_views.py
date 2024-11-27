import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from todo.models import List, ListItem, Template, TemplateItem, SharedList, ListTags
from datetime import datetime, timedelta
from django.utils.timezone import now
from io import StringIO

@pytest.fixture
def create_user():
    user = User.objects.create_user(username="testuser", password="password123")
    return user

@pytest.fixture
def authenticated_client(create_user):
    client = Client()
    client.login(username="testuser", password="password123")
    return client

@pytest.fixture
def create_list(create_user):
    return List.objects.create(
        title_text="Test List", user_id=create_user, created_on=now(), updated_on=now()
    )

@pytest.fixture
def create_template(create_user):
    return Template.objects.create(
        title_text="Test Template", user_id=create_user, created_on=now(), updated_on=now()
    )

@pytest.mark.django_db
def test_index_authenticated(authenticated_client, create_list):
    response = authenticated_client.get(reverse("todo:index"))
    assert response.status_code == 200
    assert b"Test List" in response.content

@pytest.mark.django_db
def test_index_unauthenticated():
    client = Client()
    response = client.get(reverse("todo:index"))
    assert response.status_code == 302  # Redirect to login page

@pytest.mark.django_db
def test_create_new_todo_list(authenticated_client):
    response = authenticated_client.post(reverse("todo:createNewTodoList"), {
        "list_title": "New List",
        "list_tag": "tag1"
    }, content_type="application/json")
    assert response.status_code == 200
    assert List.objects.filter(title_text="New List").exists()

@pytest.mark.django_db
def test_create_new_list_with_invalid_tag(authenticated_client):
    response = authenticated_client.post(reverse("todo:createNewTodoList"), {
        "list_title": "List with invalid tag",
        "list_tag": ""
    }, content_type="application/json")
    assert response.status_code == 200
    assert List.objects.filter(title_text="List with invalid tag").exists()

@pytest.mark.django_db
def test_add_new_list_item(authenticated_client, create_list):
    response = authenticated_client.post(reverse("todo:addNewListItem"), {
        "list_id": create_list.id,
        "list_item_name": "Test Item",
        "create_on": now().timestamp(),
        "due_date": (now() + timedelta(days=2)).strftime("%Y-%m-%d")
    }, content_type="application/json")
    assert response.status_code == 200
    assert ListItem.objects.filter(item_name="Test Item").exists()

@pytest.mark.django_db
def test_remove_list_item(authenticated_client, create_list):
    item = ListItem.objects.create(
        list=create_list, item_name="Test Item", created_on=now(), due_date=now(), finished_on=now()
    )
    response = authenticated_client.post(reverse("todo:removeListItem"), {
        "list_item_id": item.id
    }, content_type="application/json")
    assert response.status_code == 302  # Redirect after deletion
    assert not ListItem.objects.filter(id=item.id).exists()

@pytest.mark.django_db
def test_mark_list_item(authenticated_client, create_list):
    item = ListItem.objects.create(
        list=create_list, item_name="Mark Item", created_on=now(), finished_on=now(), due_date=now()
    )
    response = authenticated_client.post(reverse("todo:markListItem"), {
        "list_item_id": item.id,
        "is_done": True
    }, content_type="application/json")
    assert response.status_code == 200
    item.refresh_from_db()
    assert item.is_done

@pytest.mark.django_db
def test_update_list_item(authenticated_client, create_list):
    item = ListItem.objects.create(
        list=create_list, item_name="Update Item", created_on=now(), finished_on=now(), due_date=now()
    )
    response = authenticated_client.post(reverse("todo:updateListItem", args=[item.id]), {
        "title": "Updated Title",
        "priority": "HIGH"
    }, content_type="application/json")
    assert response.status_code == 200
    item.refresh_from_db()
    assert item.item_name == "Updated Title"
    assert item.priority == "HIGH"

@pytest.mark.django_db
def test_import_todo_csv(authenticated_client):
    csv_data = StringIO("List Title,Item Name,Item Text,Is Done,Created On,Due Date\nTest List,Item 1,Note,False,2023-11-01,2023-11-05")
    response = authenticated_client.post(reverse("todo:import_todo_csv"), {
        "csv_file": csv_data
    })
    assert response.status_code == 302  # Redirect after import
    assert List.objects.filter(title_text="Test List").exists()

@pytest.mark.django_db
def test_export_todo_csv(authenticated_client, create_list):
    ListItem.objects.create(
        list=create_list, item_name="Export Item", created_on=now(), finished_on=now(), due_date=now()
    )
    response = authenticated_client.get(reverse("todo:export_todo_csv"))
    assert response.status_code == 200
    assert b"Export Item" in response.content

@pytest.mark.django_db
def test_delete_todo_list(authenticated_client, create_list):
    response = authenticated_client.post(reverse("todo:delete_todo"), {
        "todo": create_list.id
    })
    assert response.status_code == 302  # Redirect after deletion
    assert not List.objects.filter(id=create_list.id).exists()

@pytest.mark.django_db
def test_delete_template(authenticated_client, create_template):
    response = authenticated_client.post(reverse("todo:delete_template", args=[create_template.id]))
    assert response.status_code == 302  # Redirect after deletion
    assert not Template.objects.filter(id=create_template.id).exists()

@pytest.mark.django_db
def test_login_request(create_user):
    client = Client()
    response = client.post(reverse("todo:login"), {
        "username": "testuser",
        "password": "password123"
    })
    assert response.status_code == 302  # Redirect to index on success

@pytest.mark.django_db
def test_logout_request(authenticated_client):
    response = authenticated_client.get(reverse("todo:logout"))
    assert response.status_code == 302  # Redirect to index after logout

@pytest.mark.django_db
def test_password_reset_request(create_user):
    client = Client()
    response = client.post(reverse("todo:password_reset"), {
        "email": create_user.email
    })
    assert response.status_code in [200, 302]  # Redirect to done after reset


@pytest.mark.django_db
def test_get_all_tags(authenticated_client, create_list):
  # Create tasks with tags
  ListItem.objects.create(
    list=create_list, item_name="Task 1", tags=["urgent", "work"], created_on=now()
  )
  ListItem.objects.create(
    list=create_list, item_name="Task 2", tags=["personal"], created_on=now()
  )
  response = authenticated_client.get(reverse("todo:get_tags"))

  assert response.status_code == 200
  assert response.json() == ["urgent", "work", "personal"]


@pytest.mark.django_db
def test_get_tags_empty(authenticated_client):
  response = authenticated_client.get(reverse("todo:get_tags"))

  assert response.status_code == 200
  assert response.json() == []


@pytest.mark.django_db
def test_get_tags_deduplication(authenticated_client, create_list):
  ListItem.objects.create(
    list=create_list, item_name="Task 1", tags=["urgent", "work"], created_on=now()
  )
  ListItem.objects.create(
    list=create_list, item_name="Task 2", tags=["urgent", "personal"], created_on=now()
  )
  response = authenticated_client.get(reverse("todo:get_tags"))

  assert response.status_code == 200
  assert set(response.json()) == {"urgent", "work", "personal"}


@pytest.mark.django_db
def test_filter_tasks_by_tag(authenticated_client, create_list):
  task_urgent = ListItem.objects.create(
    list=create_list, item_name="Urgent Task", tags=["urgent"], created_on=now()
  )
  ListItem.objects.create(
    list=create_list, item_name="Non-Urgent Task", tags=["non-urgent"], created_on=now()
  )

  response = authenticated_client.get(reverse("todo:filter_lists") + "?tags=urgent")

  assert response.status_code == 200
  assert len(response.context["latest_list_items"]) == 1
  assert response.context["latest_list_items"][0].id == task_urgent.id


@pytest.mark.django_db
def test_add_tags_to_task(authenticated_client, create_list):
  task = ListItem.objects.create(
    list=create_list, item_name="Taggable Task", tags=[], created_on=now()
  )
  response = authenticated_client.post(reverse("todo:updateListItem", args=[task.id]), {
    "tags": ["new-tag", "important"]
  }, content_type="application/json")

  assert response.status_code == 200
  task.refresh_from_db()
  assert set(task.tags) == {"new-tag", "important"}


@pytest.mark.django_db
def test_remove_tags_from_task(authenticated_client, create_list):
  task = ListItem.objects.create(
    list=create_list, item_name="Taggable Task", tags=["old-tag", "to-remove"], created_on=now()
  )
  response = authenticated_client.post(reverse("todo:updateListItem", args=[task.id]), {
    "tags": ["old-tag"]
  }, content_type="application/json")

  assert response.status_code == 200
  task.refresh_from_db()
  assert set(task.tags) == {"old-tag"}


@pytest.mark.django_db
def test_invalid_tags_format(authenticated_client, create_list):
  task = ListItem.objects.create(
    list=create_list, item_name="Invalid Tags Task", tags=[], created_on=now()
  )
  response = authenticated_client.post(reverse("todo:updateListItem", args=[task.id]), {
    "tags": "not-a-list"
  }, content_type="application/json")

  assert response.status_code == 400  # Bad Request
  task.refresh_from_db()
  assert task.tags == []

  
