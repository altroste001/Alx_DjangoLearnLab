from django.shortcuts import render, redirect
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

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})