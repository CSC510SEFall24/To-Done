<p align="center">
  <img src="img/todone-logo.png" />
</p>
<h2 align="center">The Only Todo List You Need</h2>

[![Build Status](https://github.com/Chloe-Ku/smart-todo/actions/workflows/django.yml/badge.svg)](https://github.com/Chloe-Ku/smart-todo/actions/workflows/django.yml)
[![Coverage Status](https://coveralls.io/repos/github/Software-Engineering-Project-PKHSAK/To-Done/badge.svg?branch=main)](https://coveralls.io/github/Software-Engineering-Project-PKHSAK/To-Done?branch=main)
[![license badge](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/Chloe-Ku/smart-todo/blob/main/LICENSE)
[![issues badge](https://img.shields.io/github/issues/Chloe-Ku/smart-todo)](https://github.com/Chloe-Ku/smart-todo/issues)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Django 4.1](https://img.shields.io/badge/django-4.1-blue.svg)](https://docs.djangoproject.com/en/4.1/releases/4.1/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14015350.svg)](https://doi.org/10.5281/zenodo.14015350)
[![Pylint](https://img.shields.io/badge/pylint-2.7.2-brightgreen.svg)](https://pylint.pycqa.org/en/latest/)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Software-Engineering-Project-PKHSAK_To-Done&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Software-Engineering-Project-PKHSAK_To-Done)


# TO-DONE
In today’s fast-paced world, keeping track of tasks and staying organized can feel overwhelming. Whether you’re juggling personal projects, work assignments, or daily chores, a clear and efficient task management system is essential. This is where To-Done comes into play.

Imagine waking up in the morning, ready to tackle the day, but feeling the weight of unfinished tasks hanging over you. You grab a cup of coffee and sit down to plan your day, but instead of clarity, you’re met with confusion—sticky notes everywhere, random lists scattered across apps, and no real sense of what to prioritize.

Now, picture this: with To-Done, you open your app and see a clean, intuitive interface. All your tasks are organized, categorized, and prioritized. You can easily add new items, set deadlines, and even collaborate with friends or colleagues. With everything in one place, you feel empowered to take on the day, knowing that you have a reliable system guiding you.

To-Done isn’t just another task manager; it’s designed to enhance productivity and simplify your life. Built for user-friendliness, it adapts to your needs, whether you’re a student, professional, or simply looking to manage daily tasks effectively.

### Ready to conquer your to-do list? With To-Done, focus on what matters and streamline your workflow. Dive in today and experience how easy task management can be!

### Watch this video to know more about TO-DONE 2.0


https://user-images.githubusercontent.com/23623764/205810552-556e0449-3f81-4e55-ad9a-414de9731b15.mp4


### Watch this video to know more about the original TO-DONE 
<img src="img/todone-create-list.gif" width="1200" height="500" />

Contents
========

 * [Why?](#why)
 * [Features](#key-features-last-version)
 * [New Features](#new-features)
 * [Upcoming Features](#upcoming-features)
 * [Quick Start](#quick-start)
 * [Documentation](#Documentation)
 * [Want to contribute?](#want-to-contribute)
 * [License](#license)
 * [Developer](#developers-new-version)

### Why?

We wanted to work on something that is:

+ Useful, serves some real purpose
+ Easy to start with a basic working version and lends itself to adding new features incrementally to it
+ Easily divisible in modules/features/tasks that can be parallely done by five developers 
+ Diverse enough so that a lot of Software Engineering practices is required/involved 

`to-done` is a todo list app that is actually useful, very easy to create a basic working version with where a ton of new features can be added, touches upon all the aspects of web programming, database, working in a team etc.

### Features 
 * [Register](#register)
 * [Login](#login-forget-password)
 * [Create, Update, Delete Todo Lists](#manage-todo-list)
 * [Quickly Create Todo Lists From Existing Templates](#templates)
 * [Create Your Own Templates](#templates)
 
### Key Features (Last Version)
 * [Shared List](#shared-todo-lists)
 * [Add Due Date To Tasks](#due-date-color-tags)
 * [Due Date Alerting Mechanism](#due-date-color-tags)
 * [Add Reminder Message to task completed](#due-date-color-tags)
 * [Customized Color Tag](#due-date-color-tags)
 * [Add Tags To Todo Lists For Customizable Grouping](#customizable-grouping-tags)

### New Features
 * [Dark Mode]
 * Social login - Google Sign-in 
 * Bugfixes

### Upcoming Features
 * Export and import to-do lists
 * Gamification - earn points by finishing your tasks, show-off your productivity in social media
 * [List of All Planned Features for Second Phase](https://github.com/users/shahleon/projects/2/views/6)

### Quick Start

 * Please refer to INSTALL.md for setting up & running this project
 
### Documentation
[See this page](https://chloe-ku.github.io/smart-todo/)

### Features

#### Register
<p float="middle">
    <img src="img/todone-register.gif" width="500" height="250" />
</p>

#### Login, Forget Password
<p float="middle">
    <img src="img/todone-login.gif" width="500" height="250" /> 
</p>

#### Manage Todo List
<p float="middle">
    <img src="img/todone-create-list.gif" width="500" height="250" />
    <br>
    <br>
    <img src="img/todone-update-list.gif" width="500" height="250" />
</p>

#### Templates
<p float="middle">
    <img src="img/todone-templates.gif" width="500" height="250" />
</p>

### New Features
#### Customizable Grouping Tags
<p float="middle">
    <img src="img/todone-tag-list.gif" width="500" height="250" />
</p>

#### Shared ToDo Lists
<p float="middle">
    <img src="img/todone-shared-list.gif" width="500" height="250" />
</p>

#### Due Date, Color Tags
<p float="middle">
    <img src="img/todone-tag-color.gif" width="500" height="250" />
</p>

# Future Scope

## 3 month Tasks
1) ### Task Creation and Management:
   Enhance the task creation interface with fields for due dates and priority levels.
   Implementing basic task editing and deletion functionalities.

2) ### User Interface Improvements:
   Conduct user testing to gather feedback on the current UI.
   Make initial UI improvements based on user feedback.

3) ### Basic Notifications:
   Implement email notifications for task deadlines.

## 6 month Tasks
1) ### Collaboration Features
   Develop shared tasks functionality to allow users to collaborate on projects.
   Implement a commenting system for tasks.

2) ### Task Prioritization and Categorization
   Introduce tagging and categorization for tasks.
   Implement priority levels for tasks.

3) ### Enhanced User Interface
    Implement responsive design for mobile compatibility.
    Introduce a dark mode option.

## 12 month Tasks
1) ### Mobile Application Development
    Develop and launch a mobile application for iOS and Android.

2) ### Advanced Search and Filtering
    Implement a robust search feature for tasks.
    Develop filtering options based on date, priority, and category.

3) ### Customizable Dashboards
    Allow users to customize their dashboard layout and displayed information.

### Want to Contribute?

Want to contribute to this project? Learn about [Contributing](CONTRIBUTING.md). Not sure where to start? Have a look at 
the [good first issue](https://github.com/shahleon/smart-todo/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22). Found a bug or have a new feature idea? Please create an [Issue](https://github.com/Chloe-Ku/smart-todo/issues) to notify us.

### License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

### Developers (New Version)

<table>
  <tr>
    <td align="center"><a href="https://github.com/akarsh16reddy"><img src="https://avatars.githubusercontent.com/u/63505953?v=4" width="100px;" alt=""/><br /><sub><b>Akarsh Reddy, Eathamukkala</b></sub></a></td>
    <td align="center"><a href="https://github.com/PrateekKamath"><img src="https://avatars.githubusercontent.com/u/92785050?v=4" width="100px;" alt=""/><br /><sub><b>Prateek Kamath</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/123standup"><img src="https://avatars.githubusercontent.com/u/24963056?v=4" width="100px;" alt=""/><br /><sub><b>Himanshu Singh</b></sub></a><br /></td>
  </tr>
</table>

### Developers (Last Version)

* Chiu, Ching-Lun (https://github.com/juliachiu1)
* Yu, Hsueh-Yang (https://github.com/Hsueh-YANG)
* Lin, Po-Hsun (https://github.com/123standup)
* Ku, Li-Ling (https://github.com/Chloe-Ku)
* Chiang, Chen-Hsuan (https://github.com/jackson910210)
