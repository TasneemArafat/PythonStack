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
                messages.success(request, "successfully registered (or logged in)!")
                return redirect('/welcome')
        return redirect('/')

def welcome(request):
    if "id" in request.session:
        return render(request,'welcome.html')
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
                return redirect('/welcome')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')