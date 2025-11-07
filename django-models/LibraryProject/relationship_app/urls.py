from django.http import HttpResponse
from .models import Book
from django.shortcuts import render



def list_books(request):
    
    books = Book.objects.all()
    
    context = {'books': books }
    
    return render(request, 'relationship_app/list_books.html', context)


