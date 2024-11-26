import pytest
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from todo.models import List, ListItem, Template, SharedList, ListTags, TemplateItem
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from todo.views import config, config_hook, delete_template, login_request, template_from_todo, template, delete_todo, index, getListTagsByUserid, removeListItem, addNewListItem, updateListItem, createNewTodoList, register_request, getListItemByName, getListItemById, markListItem, todo_from_template
from todo.forms import NewUserForm
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages import get_messages


@pytest.mark.django_db
class TestTodoAppViews:

    def setup_method(self):
        # Common setup for tests
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.other_user = User.objects.create_user(username="otheruser", password="otherpass")
        self.list = List.objects.create(
            user_id=self.user,
            title_text="Test List",
            created_on=timezone.now(),
            updated_on=timezone.now()
        )
        self.list_item = ListItem.objects.create(
            list=self.list,
            item_name="Test Item",
            created_on=timezone.now(),
            finished_on=timezone.now(),
            due_date=timezone.now(),
            priority="High",
            is_done=False,
        )
        self.template = Template.objects.create(
            user_id=self.user,
            title_text="Test Template",
            created_on=timezone.now(),
            updated_on=timezone.now()
        )
        self.template_item = TemplateItem.objects.create(
            template=self.template,
            item_text="Test Template Item",
            created_on=timezone.now(),
            finished_on=timezone.now(),
            due_date=timezone.now(),
            priority="Medium",
        )
        SharedList.objects.create(user=self.user, shared_list_id="")

    def test_index_authenticated(self, client):
        client.login(username="testuser", password="testpass")
        response = client.get(reverse("todo:index"))
        assert response.status_code == 200
        assert "Test List" in response.content.decode()

    def test_index_redirects_for_anonymous(self, client):
        response = client.get(reverse("todo:index"))
        assert response.status_code == 302
        assert "/login" in response.url

    def test_create_new_todo_list(self, client):
        client.login(username="testuser", password="testpass")
        response = client.post(reverse("todo:createNewTodoList"), data={
            "list_name": "New Test List",
            "create_on": timezone.now().timestamp(),
            "list_tag": "Test Tag",
            "shared_user": "",
            "create_new_tag": True
        }, content_type="application/json")
        assert response.status_code == 200
        assert List.objects.filter(title_text="New Test List").exists()

    def test_update_list_item(self, client):
        client.login(username="testuser", password="testpass")
        url = reverse("todo:updateListItem", kwargs={"item_id": self.list_item.id})
        response = client.post(url, data={
            "item_name": "Updated Item",
            "item_description": "Updated Description",
            "due_date": timezone.now().strftime("%Y-%m-%d"),
            "priority": "Medium",
        })
        assert response.status_code == 200
        updated_item = ListItem.objects.get(id=self.list_item.id)
        assert updated_item.item_name == "Updated Item"

    def test_delete_todo_item(self, client):
        client.login(username="testuser", password="testpass")
        response = client.post(reverse("todo:delete_todo"), data={
            "todo": self.list.id
        })
        assert response.status_code == 302
        assert not List.objects.filter(id=self.list.id).exists()

    def test_create_template_from_todo(self, client):
        client.login(username="testuser", password="testpass")
        response = client.post(reverse("todo:template_from_todo"), data={
            "todo": self.list.id
        })
        assert response.status_code == 302
        assert Template.objects.filter(title_text="Test List").exists()

    #def test_import_todo_csv_invalid_format(self, client, tmpdir):
        #client.login(username="testuser", password="testpass")
       # file_path = tmpdir.join("invalid_todo.csv")
        #with open(file_path, "w") as f:
         #   f.write("Invalid,CSV,Format")
        #with open(file_path, "rb") as f:
         #   response = client.post(reverse("todo:import_todo_csv"), data={"csv_file": f})
        #assert response.status_code == 302
        #assert "Invalid CSV format" in [m.message for m in response.wsgi_request._messages]

    def test_template_list(self, client):
        client.login(username="testuser", password="testpass")
        response = client.get(reverse("todo:template"))
        assert response.status_code == 200
        assert "Test Template" in response.content.decode()

    def test_delete_template(self, client):
        client.login(username="testuser", password="testpass")
        response = client.post(reverse("todo:delete_template", args=[self.template.id]))
        assert response.status_code == 302
        assert not Template.objects.filter(id=self.template.id).exists()

    #def test_social_login_redirects_invalid_token(self, client):
     #   response = client.post(reverse("todo:social_login"), data={
      #      "credential": "invalid_token"
       # })
        #assert response.status_code == 302
        #assert "Invalid token" in [m.message for m in response.wsgi_request._messages]
