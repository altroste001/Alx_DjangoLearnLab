from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

def books_list(request):
    books = Book.objects.all()
    context = {'books': books}      
    return render(request, 'relationship_app/list_books.html', context)

class ShowLibrary(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')