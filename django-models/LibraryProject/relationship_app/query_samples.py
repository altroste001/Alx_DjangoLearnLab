from relationship_app.models import Author, Book, Librarian, Library

author = Author.objects.first()
books_by_author  = author.book_set.all()

    
library = Library.objects.first()
books_in_library  = library.books.all()
    


librarian = library.librarian




