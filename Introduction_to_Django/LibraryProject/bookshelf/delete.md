from bookshelf.models import Book

e
book = Book.objects.get(title='Nineteen Eighty-Four')


book.delete()


Book.objects.all()

# Expected Output:
# <QuerySet []>
