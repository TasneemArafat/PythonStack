from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    context={
        "all_books":all_books()
    }
    return render(request,"index.html",context)

def add_book(request):
    if request.method == "POST":
        addbook(request.POST)
    return redirect('/')

def view_book(request,id):
    context= {
        "this_book":x_book(id),
        "all_authors":all_authors()
    }
    request.session['id']=x_book(id).id
    return render(request,'book.html',context)

def show_authors(request):
    context={
        "all_authors":all_authors()
        }
    return render(request,"authors.html",context)

def add_author(request):
    if request.method == "POST":
        addauthor(request.POST)
    return redirect('/authors')

def view_author(request,id):
    context= {
        "this_author":x_author(id),
        "all_books":all_books()
    }
    return render(request,'author.html',context)

def select_author(request):
    if request.method == "POST":
        selectauthor(request.POST)
        value ="books/"+request.POST['this_book']
    return redirect(value)

def select_book(request):
    if request.method == "POST":
        selectbook(request.POST)
        value ="author/"+request.POST['this_author']
    return redirect(value)
