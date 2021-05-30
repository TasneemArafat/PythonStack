from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    errors = models.User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        if request.method == "POST":
            firstname = request.POST['fname']
            lastname = request.POST['lname']
            Email = request.POST['email']
            Password = request.POST['passwd']
            Confirm = request.POST['confpasswd']
            if Password == Confirm:
                password = request.POST['passwd']
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
                user = models.create_user(firstname,lastname,Email,pw_hash)
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                return redirect('/books')
        return redirect('/')

def books(request):
    if "id" in request.session:
        context={
            'all_books':models.all_books(),
            'fav_books':models.my_favourites(request.session['id'])
        }
        return render(request,'welcome.html',context)
    return redirect('/')

def login(request):
    errors = models.User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect('/')
    else:
        print("NO ERRORS")
        if request.method == "POST":
            Email = request.POST['email']
            Password = request.POST['passwd']
            user = models.get_user(Email)
            if user:
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['last_name'] = user.last_name
                return redirect('/books')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def add_fav_book(request):
    if request.method == "POST":
        errors = models.Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/books')
        else:
                title = request.POST['title']
                desc = request.POST['desc']
                user = request.POST['user']
                book = models.add_book(title,desc,user)
                return redirect(f'/books/{book.id}')
    return redirect('/books')

def show_book(request,book_id):
    context={
        "this_book":models.Book.objects.get(id=book_id),
        "book_liked_by":models.book_liked_by(request.session['id'],book_id)
    }
    return render(request,"book.html",context)

def update_book(request,book_id):
    if request.method=='POST':
        errors = models.Book.objects.book_update_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect(f'/books/{book_id}')
        else:
            new_desc=request.POST['desc']
            models.Update_book(new_desc,book_id)
            return redirect(f'/books/{book_id}') 
    return redirect(f'/books/{book_id}')      

def delete_book(request,book_id):
    models.Delete_book(book_id)
    return redirect('/books')

def remove_from_fav(request,book_id):
    user_id=request.session['id']
    models.remove_from_fav(user_id,book_id)
    return redirect(f'/books/{book_id}')

def add_to_fav(request,book_id):
    user_id=request.session['id']
    models.add_to_fav(user_id,book_id)
    return redirect(f'/books/{book_id}')





