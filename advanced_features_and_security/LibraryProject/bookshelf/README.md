# Task 1: Managing Permissions and Groups in Django

This task implements a permission-based access control system in the `bookshelf` app.

## 1. Custom Permissions in the Book Model

The `Book` model defines four custom permissions inside its `Meta` class:

class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]
