from django.db import models

# Create your models here.
from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        if len(postData['fname']) < 2 :
            errors["fname-length"] = "First Name should be at least 2 characters"
        if not NAME_REGEX.match(postData['fname']):
            errors["fname-char"] = "First Name should only contain characters"
        if len(postData['lname']) < 2:
            errors["lname-length"] = "Last Name should be at least 2 characters"
        if not NAME_REGEX.match(postData['lname']):
            errors["lname-char"] = "Last Name should only contain characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['passwd']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['passwd'] != postData['confpasswd']:
            errors['confpasswd'] = "Password doesn't match Confirm Password"
        return errors
    def login_validator(self,postData):
        errors = {}
        users = User.objects.filter(Email=postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not len(users):
            errors['email'] = "Email not Found!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        elif not bcrypt.checkpw(postData['passwd'].encode(), users[0].Password.encode()):
            errors["password"] = "Wrong Password!"
        return errors
    def book_validator(self,postData):
        errors = {}
        books = Book.objects.filter(title=postData['title'])
        if not postData['title']:
            errors['title'] = "Title is required!"
        if len(books):
            errors['title'] = "Book already added!"
        if len(postData['desc'])< 5:
            errors['desc'] = "Description should be at least 5 characters"
        return errors
    def book_update_validator(self,postData):
        errors = {}
        if len(postData['desc'])< 5:
            errors['desc'] = "Description should be at least 5 characters"
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    Email = models.CharField(max_length=225)
    Password = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=225)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    user_uploaded = models.ForeignKey(User,related_name="books",on_delete = models.CASCADE)
    user_liked = models.ManyToManyField(User,related_name="liked_books")
    objects = UserManager()

def create_user(first_name,last_name,email,passwd):
    return User.objects.create(first_name=first_name,last_name=last_name,Email=email,Password=passwd)

def get_user(email):
    users = User.objects.filter(Email=email)
    if len(users) > 0:
        return users[0]
    return None

def add_book(title,desc,uploaded_by):
    user=User.objects.get(id=uploaded_by)
    book = Book.objects.create(title=title,desc=desc,user_uploaded=user)
    book.user_liked.add(user)
    return book

def all_books():
    all_books=Book.objects.all()
    return all_books

def Update_book(new_desc,id):
    book_to_update=Book.objects.get(id=id)
    book_to_update.desc = new_desc
    book_to_update.save()

def Delete_book(id):
    book_to_delete = Book.objects.get(id=id)
    book_to_delete.delete()

def book_liked_by(user_id,book_id):
    book = Book.objects.get(id=book_id)
    book_liked_by = book.user_liked.all()
    users = book_liked_by.filter(id=user_id)
    return users
    # book = Book.objects.get(id=id)
    # all_favs = book.user_liked.all()
    # for i in all_favs:
    #     if i.id == user_id:
    #         return True
    # return False

def remove_from_fav(user_id,book_id):
    book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id=user_id)
    book.user_liked.remove(this_user)

def add_to_fav(user_id,book_id):
    book = Book.objects.get(id=book_id)
    this_user = User.objects.get(id=user_id)
    book.user_liked.add(this_user)

def my_favourites(user_id):
    user=User.objects.get(id=user_id)
    My_liked_books=user.liked_books.all()
    return(My_liked_books)

    