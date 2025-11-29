## 2. View Configuration & Behavior

This project uses Django REST Framework to expose API endpoints for managing authors and books.
The views are a mix of low-level `APIView` classes and generic class-based views.

### 2.1 Author Views

#### `AuthorListView` (GET /api/authors/)

- **Type:** `APIView`
- **Purpose:** Returns a list of all authors in the system.
- **Behavior:**
  - Fetches all `Author` objects from the database.
  - Serializes them using `AuthorSerializer`.
  - Returns a JSON array of authors with HTTP 200 OK.

#### `AuthorCreateView` (POST /api/authors/create/)

- **Type:** `APIView`
- **Purpose:** Creates a new author.
- **Behavior:**
  - Accepts JSON payload matching `AuthorSerializer` fields.
  - Validates input using `serializer.is_valid()`.
  - On success, saves the new author instance and returns the created object with HTTP 201 Created.
  - On validation failure, returns error messages with HTTP 400 Bad Request.

- **Extension points:**
  - Custom creation logic (e.g., setting default fields) can be added by extending the `post()` method
    before or after `serializer.save()`.

---

### 2.2 Book Views

#### `BookListCreateView` (GET /api/books/, POST /api/books/)

- **Type:** `ListCreateAPIView`
- **Purpose:** 
  - `GET` → List all books
  - `POST` → Create a new book

- **Queryset & Serializer:**
  - `queryset = Book.objects.all()`
  - `serializer_class = BookSerializer`

- **Filtering, Searching, and Ordering:**
  - The view is configured with DRF’s filter backends:

    ```python
    filter_backends = [
        filters.DjangoFilterBackend,
        drf_filters.SearchFilter,
        drf_filters.OrderingFilter,
    ]
    ```

  - **Filtering:**
    - Implemented with `filterset_fields`:
      ```python
      filterset_fields = ['title', 'author', 'published_date']
      ```
    - Examples:
      - `GET /api/books/?author=3`
      - `GET /api/books/?title=Harry%20Potter`
      - `GET /api/books/?published_date=2020-01-01`

  - **Searching:**
    - Implemented with `search_fields`:
      ```python
      search_fields = ['title', 'description']
      ```
    - Uses DRF’s `SearchFilter` for partial, case-insensitive search.
    - Examples:
      - `GET /api/books/?search=magic`
      - `GET /api/books/?search=rowling`

  - **Ordering:**
    - Implemented with `ordering_fields`:
      ```python
      ordering_fields = ['title', 'published_date']
      ```
    - Examples:
      - `GET /api/books/?ordering=title` (A → Z by title)
      - `GET /api/books/?ordering=-published_date` (newest first)

- **Custom settings / hooks:**
  - `filter_backends` changes the default behavior of `ListCreateAPIView` by enabling
    dynamic filtering, searching, and ordering from query parameters.
  - To customize creation behavior, you can override:
    ```python
    def perform_create(self, serializer):
        # custom logic before saving
        serializer.save()
    ```

---

#### `BookDetailView` (GET /api/books/<id>/, PUT/PATCH, DELETE)

- **Type:** `RetrieveUpdateDestroyAPIView`
- **Purpose:** Retrieve, update, or delete a single book instance.

- **Behavior:**
  - Looks up a book by primary key (`pk`) from the URL.
  - `GET` → Returns serialized book data.
  - `PUT/PATCH` → Validates and updates the book.
  - `DELETE` → Deletes the book and returns HTTP 204 No Content.

- **Custom settings / hooks:**
  - The default behavior can be extended using:
    - `get_queryset()` to change how the book is retrieved.
    - `perform_update(serializer)` for custom update behavior.
    - `perform_destroy(instance)` for custom delete behavior.

---

### 2.3 Global Configuration

The API uses DRF’s default filter backends configured at the view level (not globally in `settings.py`).
The `BookListCreateView` explicitly declares which fields are available for filtering, searching, and ordering.

No custom global hooks are currently used beyond the standard DRF and `django-filter` configuration.


/////



🔹 Task 2: Filtering, Searching, and Ordering

This task adds advanced query capabilities to the Book API endpoint using Django REST Framework and django-filter.

✔ Installed dependency
pip install django-filter

✔ Updated REST Framework configuration (settings.py)
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}

DJANGO_FILTERS_DISABLE_HELP_TEXT = True

✔ Updated BookListView in api/views.py
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

✔ How to use the new features
🔎 Filtering
/api/books/?publication_year=2020
/api/books/?author=1

🔍 Searching
/api/books/?search=harry
/api/books/?search=Test

🔽 Ordering
/api/books/?ordering=title
/api/books/?ordering=-publication_year

✔ Example JSON response
[
  {
    "id": 1,
    "title": "Test Book",
    "publication_year": 2020,
    "author": 1
  }
]