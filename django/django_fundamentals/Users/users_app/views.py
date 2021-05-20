from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        "all_users": users_obj()
    }
    return render(request,"index.html",context)

def add_user(request):
    Users.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],email_address= request.POST["email"],age = request.POST["age"])
    return redirect('/')
