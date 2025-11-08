from django.urls import path
from .views import books_list, ShowLibrary

urlpatterns = [
    path('', books_list, name='home'),
    path('books/', books_list, name='books_list'),
    path('library/<int:pk>/', ShowLibrary.as_view(), name='library_detail'),
]
