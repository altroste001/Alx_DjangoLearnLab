from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title='Nineteen Eighty-Four')

# Delete the book
book.delete()

# Retrieve all books to confirm deletion
Book.objects.all()

# Expected Output:
# <QuerySet []>
