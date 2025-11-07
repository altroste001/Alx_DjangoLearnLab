from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView

def books_list(request):
    books = Book.objects.all()
    context = {'book_list' : books}
    return render(request, 'book/book_list.html',context)

class ShowLibrary(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    

    

