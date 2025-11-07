from django.shortcuts import render
from .models import Book, Library  
from django.views.generic import DetailView


def books_list(request):
    books = Book.objects.all()
    context = {'books': books}      
    return render(request, 'list_books.html', context)  

class ShowLibrary(DetailView):
    model = Library
    template_name = "library_detail.html"  
    context_object_name = "library"       


