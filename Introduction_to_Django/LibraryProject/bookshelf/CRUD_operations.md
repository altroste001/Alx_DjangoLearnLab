from bookshelf.models import Book
book = Book.objects.create(title='1984' , author='George Orwell' , publication_year=1949)

Book.objects.get()

book.title = "Nineteen Eighty-Four"
book.save()

book.delete()
