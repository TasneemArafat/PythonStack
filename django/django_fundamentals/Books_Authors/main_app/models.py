from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    book = models.ManyToManyField(Book, related_name="books")
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def all_books():
    books = Book.objects.all()
    return(books)

def addbook(input):
    new_book = Book.objects.create(title=input['title'],desc=input['desc'])
    return(new_book)

def x_book(i):
    book = Book.objects.get(id=i)
    return book

def all_authors():
    authors = Author.objects.all()
    return(authors)

def addauthor(input):
    new_author = Author.objects.create(first_name=input['fname'],last_name=input['lname'],notes=input['notes'])
    return(new_author)

def x_author(i):
    author = Author.objects.get(id=i)
    return author

def selectauthor(input):
    this_book = Book.objects.get(id=input['this_book'])
    this_author = Author.objects.get(first_name=input['selected_author'])
    this_book.books.add(this_author)
    return this_book

def selectbook(input):
    this_author = Author.objects.get(id=input['this_author'])
    this_book = Book.objects.get(title=input['selected_book'])
    this_author.book.add(this_book)
    return this_author