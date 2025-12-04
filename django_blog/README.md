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
