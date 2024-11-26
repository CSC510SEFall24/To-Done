import pytest
from django.utils import timezone
from django.contrib.auth.models import User
from todo.models import List, ListTags, ListItem, Template, TemplateItem, SharedUsers, SharedList
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from todo.views import config, config_hook, delete_template, login_request, template_from_todo, template, delete_todo, index, getListTagsByUserid, removeListItem, addNewListItem, updateListItem, createNewTodoList, register_request, getListItemByName, getListItemById, markListItem, todo_from_template
from todo.forms import NewUserForm
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages import get_messages


@pytest.mark.django_db
class TestTodoModels:

    def setup_method(self):
        # Setup common objects for tests
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.other_user = User.objects.create_user(username="otheruser", password="otherpass")
        self.list = List.objects.create(
            title_text="Test List",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            list_tag="Test Tag",
            user_id=self.user,
            is_shared=False
        )
        self.list_item = ListItem.objects.create(
            list=self.list,
            item_name="Test Item",
            item_desc="Test Description",
            item_text="Test Item Text",
            is_done=False,
            created_on=timezone.now(),
            finished_on=timezone.now(),
            due_date=timezone.now().date(),
            priority="High"
        )
        self.template = Template.objects.create(
            title_text="Test Template",
            created_on=timezone.now(),
            updated_on=timezone.now(),
            user_id=self.user
        )
        self.template_item = TemplateItem.objects.create(
            template=self.template,
            item_text="Test Template Item",
            created_on=timezone.now(),
            finished_on=timezone.now(),
            due_date=timezone.now().date(),
            priority="Medium"
        )
        self.shared_user = SharedUsers.objects.create(
            list_id=self.list,
            shared_user="shared_user@example.com"
        )
        self.shared_list = SharedList.objects.create(
            user=self.user,
            shared_list_id="1 2 3"
        )
        self.list_tag = ListTags.objects.create(
            user_id=self.user,
            tag_name="Important",
            created_on=timezone.now()
        )

    # Test cases for List model
    def test_list_creation(self):
        assert List.objects.count() == 1
        assert self.list.title_text == "Test List"

    def test_list_str(self):
        assert str(self.list) == "Test List"

    def test_list_is_shared_default(self):
        assert not self.list.is_shared

    def test_list_tag(self):
        assert self.list.list_tag == "Test Tag"

    # Test cases for ListItem model
    def test_list_item_creation(self):
        assert ListItem.objects.count() == 1
        assert self.list_item.item_name == "Test Item"

    def test_list_item_priority(self):
        assert self.list_item.priority == "High"

    def test_list_item_str(self):
        assert str(self.list_item) == "Test Item Text: False"

    def test_list_item_is_done_default(self):
        assert not self.list_item.is_done

    # Test cases for Template model
    def test_template_creation(self):
        assert Template.objects.count() == 1
        assert self.template.title_text == "Test Template"

    def test_template_str(self):
        assert str(self.template) == "Test Template"

    # Test cases for TemplateItem model
    def test_template_item_creation(self):
        assert TemplateItem.objects.count() == 1
        assert self.template_item.item_text == "Test Template Item"

    def test_template_item_priority(self):
        assert self.template_item.priority == "Medium"

    def test_template_item_str(self):
        assert str(self.template_item) == "Test Template Item"

    # Test cases for SharedUsers model
    def test_shared_user_creation(self):
        assert SharedUsers.objects.count() == 1
        assert self.shared_user.shared_user == "shared_user@example.com"

    # Test cases for SharedList model
    def test_shared_list_creation(self):
        assert SharedList.objects.count() == 1
        assert self.shared_list.shared_list_id == "1 2 3"

    def test_shared_list_str(self):
        assert str(self.shared_list) == str(self.user)

    # Test cases for ListTags model
    def test_list_tag_creation(self):
        assert ListTags.objects.count() == 1
        assert self.list_tag.tag_name == "Important"

    def test_list_tag_str(self):
        assert str(self.list_tag) == "Important"

    # Additional edge cases and validations
    def test_list_no_user(self):
        list_without_user = List.objects.create(
            title_text="No User List",
            created_on=timezone.now(),
            updated_on=timezone.now()
        )
        assert list_without_user.user_id is None

    def test_list_item_no_description(self):
        list_item_no_desc = ListItem.objects.create(
            list=self.list,
            item_name="No Desc Item",
            created_on=timezone.now(),
            finished_on=timezone.now(),
            due_date=timezone.now().date(),
            priority="Low"
        )
        assert list_item_no_desc.item_desc is None

    def test_template_no_user(self):
        template_without_user = Template.objects.create(
            title_text="No User Template",
            created_on=timezone.now(),
            updated_on=timezone.now()
        )
        assert template_without_user.user_id is None

    def test_shared_list_no_user(self):
        shared_list_no_user = SharedList.objects.create(
            shared_list_id="4 5 6"
        )
        assert shared_list_no_user.user is None

    def test_list_tags_no_tag_name(self):
        tag_no_name = ListTags.objects.create(
            user_id=self.user,
            created_on=timezone.now()
        )
        assert tag_no_name.tag_name is None
