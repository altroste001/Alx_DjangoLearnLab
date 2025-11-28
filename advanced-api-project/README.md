Filtering, Searching, and Ordering – Implementation Details

This project uses Django REST Framework’s built-in tools for filtering, searching, and ordering API results. These features allow the client to query data more efficiently and retrieve only what they need.

All features are activated in settings.py:

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
        'django_filters.rest_framework.DjangoFilterBackend',
    ]
}

-------------------------------------------------------------
1. Filtering

Filtering allows API users to return items that match specific fields.

Book Filtering

Enabled inside the BookListCreateView:

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['author', 'published_date', 'title']

How to use it (API examples):

Filter books by author:

GET /api/books/?author=3


Filter by title:

GET /api/books/?title=Harry%20Potter


Filter by published year:

GET /api/books/?published_date=2020-01-01

2. Searching

Searching allows partial text matching.

Enabled using:

from rest_framework import generics, filters

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['title', 'description']

How to use it:

Search by keyword:

GET /api/books/?search=magic


Search by title:

GET /api/books/?search=harry


This performs a case-insensitive match.

3. Ordering

Ordering allows the client to sort results dynamically.

Enabled inside the same view:

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_fields = ['title', 'published_date']

How to use it:

Order by title (A → Z):

GET /api/books/?ordering=title


Order by newest first:

GET /api/books/?ordering=-published_date