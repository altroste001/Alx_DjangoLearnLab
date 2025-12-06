# Django Blog Project  
ALX Django Learn Lab – Building a Complete Django Application

This project is part of the ALX Backend Learn Lab.  
It guides learners through building a fully functional **blog application** using Django.  
Each task builds on the previous one, covering everything from project setup to user authentication, CRUD operations, comments, tagging, and search.

---

## 📌 Project Overview

The Django Blog App allows users to:

- Register and create an account  
- Log in and log out  
- View and update their profile  
- (Coming in Task 2) Create, update, and delete blog posts  
- (Coming in Task 3) Add comments to posts  
- (Coming in Task 4) Add tags and use search functionality  

This README describes the environment setup and the tasks completed so far.

---

## 📁 Project Structure

django_blog/
├── blog/
│ ├── templates/blog/
│ │ ├── base.html
│ │ ├── login.html
│ │ ├── register.html
│ │ └── profile.html
│ │
│ ├── static/
│ │ ├── css/styles.css
│ │ └── js/scripts.js
│ │
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ ├── urls.py
│
├── django_blog/
│ ├── settings.py
│ └── urls.py
│
└── manage.py

---

## 🧩 Task 0: Project Setup

Completed:

✔ Created Django project `django_blog`  
✔ Created app `blog`  
✔ Added `Post` model  
✔ Configured static files  
✔ Set up template directories  
✔ Applied migrations  

---

## 🧩 Task 1: User Authentication System

Completed:

✔ Registration page  
✔ Login and logout  
✔ Profile page  
✔ Custom user creation form  
✔ Authentication templates  
✔ Updated URLs and views  
✔ Proper redirects after login and logout  

Users can now create an account, log in, and manage their profile.

---

## 🔧 Technologies Used

- Python 3  
- Django 5  
- SQLite (default database)  
- HTML / CSS / JavaScript  
- Django template engine  

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies:
```bash
pip install -r requirements.txt

2️⃣ Run migrations:
python manage.py makemigrations
python manage.py migrate

3️⃣ Start development server:
python manage.py runserver

The project will be available at:
http://127.0.0.1:8000/

🧪 Testing Authentication Features

Visit /register/ to create a new user

Visit /login/ to authenticate

Visit /profile/ to update your email

Visit /logout/ to log out

📌 Upcoming Tasks
Task 2: Blog Post Management (CRUD)

CreateView

UpdateView

DeleteView

List & Detail Views

Task 3: Comment Functionality
Task 4: Tagging and Search

Each task will be added to this README as development progresses.


🧩 Task 4: Tagging and Search Functionality

This task enhances the Django Blog by adding:

A complete tagging system

The ability to search posts based on title, content, or tags

New views, templates, and URL routes

UI integration for tags and a search bar

✔ 1. Tag Model & Relationship

A new Tag model was introduced with:

name (unique)

slug (auto-generated for URL routing)

Each Post now has:

tags = models.ManyToManyField(Tag, related_name='posts', blank=True)


This allows multiple tags per post.

✔ 2. Updated PostForm With Tags Input

The PostForm accepts a comma-separated list of tags:

django, backend, alx


These are parsed, normalized, and stored as Tag objects.

Editing a post shows its existing tags automatically.

✔ 3. Tag Display in Templates

Tags are now shown on:

Post list page

Post detail page

Each tag is a clickable link leading to:

/tags/<tag_slug>/

✔ 4. Tag Filtering View

A new view displays all posts that share a tag:

def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = tag.posts.all()
    return render(request, "blog/post_by_tag.html", { "tag": tag, "posts": posts })


Template: post_by_tag.html

✔ 5. Search Functionality

Added a global search bar in base.html.

Search view supports:

Title

Content

Tag name

Using Django’s Q objects:

results = Post.objects.filter(
    Q(title__icontains=query) |
    Q(content__icontains=query) |
    Q(tags__name__icontains=query)
).distinct()


Template: post_search.html

✔ 6. URL Routes

Added URLs:

path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts-by-tag'),
path('search/', views.post_search, name='post-search'),

✔ 7. Testing

All features were tested:

Create/update posts with tags

Display tags in templates

Filter posts by tag

Search by title/content/tags

Check template rendering

Confirm no redirect errors

Everything works as expected.
