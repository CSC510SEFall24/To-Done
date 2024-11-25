# MIT License

# Copyright © 2024 Akarsh Reddy Eathamukkala

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to
# do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    title_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    list_tag = models.CharField(max_length=50, default='none')
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    is_shared = models.BooleanField(default=False) #progress (sharing list between users)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title_text


class ListTags(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    tag_name = models.CharField(max_length=50, null=True, blank=True)
    created_on = models.DateTimeField()

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.tag_name


PRIORITY_CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
]

class ListItem(models.Model):
    # the name of a list item
    item_name = models.CharField(max_length=50, null=True, blank=True)
    # the text note of a list item
    item_desc = models.CharField(max_length=250,null=True, blank=True)
    item_text = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    created_on = models.DateTimeField()
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    finished_on = models.DateTimeField()
    due_date = models.DateField()
    tag_color = models.CharField(max_length=10)
    # Add this new field
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Low',  # Default priority
    )

    objects = models.Manager()

    def __str__(self):
        return "%s: %s" % (str(self.item_text), self.is_done)


class Template(models.Model):
    title_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.title_text


class TemplateItem(models.Model):
    item_text = models.CharField(max_length=100)
    created_on = models.DateTimeField()
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    finished_on = models.DateTimeField()
    due_date = models.DateField()
    tag_color = models.CharField(max_length=10)

    objects = models.Manager()

    def __str__(self):
        return "%s" % self.item_text

#shared users for a list
class SharedUsers(models.Model):
    list_id = models.ForeignKey(List, on_delete=models.CASCADE)
    shared_user = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return "%s" % str(self.list_id)

#shared or common lists
class SharedList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    shared_list_id = models.CharField(max_length=200)

    objects = models.Manager()

    def __str__(self):
        return "%s" % str(self.user)
