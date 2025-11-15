from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.utils.html import strip_tags


# Add Content Security Policy header to each response 
def add_csp(response):
    response["Content-Security-Policy"] = "default-src 'self'"
    return response


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    response = render(request, 'bookshelf/book_list.html', {'books': books})
    return add_csp(response)   


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":

        #Input validation and sanitization 
        title = strip_tags(request.POST.get("title", "").strip())
        author = strip_tags(request.POST.get("author", "").strip())
        publication_year = strip_tags(request.POST.get("publication_year", "").strip())

        # Using Django ORM prevents SQL injection
        Book.objects.create(
            title=title,
            author=author,
            publication_year=publication_year
        )
        return redirect("book_list")
    
    response = render(request, 'bookshelf/form_example.html')
    return add_csp(response)


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == "POST":

         # Input validation and sanitization 
        book.title = strip_tags(request.POST.get("title", "").strip())
        book.author = strip_tags(request.POST.get("author", "").strip())
        book.publication_year = strip_tags(request.POST.get("publication_year", "").strip())

        book.save()
        return redirect("book_list")
    
    response = render(request, 'bookshelf/form_example.html', {'book': book})
    return add_csp(response)


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")
