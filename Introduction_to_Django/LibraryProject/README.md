# LibraryProject

This is a Django project created as part of the ALX Django Learning Lab.

## Project Setup

This project was created using Django and includes the basic project structure.

## Installation

1. Install Django:
```
   pip install django
```

2. Run the development server:
```
   python manage.py runserver
```

3. Access the application at `http://127.0.0.1:8000/`

## Project Structure

- `manage.py`: Command-line utility for Django project management
- `LibraryProject/settings.py`: Project configuration file
- `LibraryProject/urls.py`: URL routing configuration
```

**3. Verify your project structure looks like this:**
```
Introduction_to_Django/
└── LibraryProject/
    ├── README.md              # Must exist and be non-empty
    ├── manage.py              # Must exist
    └── LibraryProject/        # Inner directory
        ├── __init__.py
        ├── settings.py        # Must exist
        ├── urls.py
        ├── asgi.py
        └── wsgi.py