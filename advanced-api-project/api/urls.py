from django.urls import path
from .views import (
    AuthorListView,
    AuthorCreateView,
    BookListCreateView,
    BookDetailView
)

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
