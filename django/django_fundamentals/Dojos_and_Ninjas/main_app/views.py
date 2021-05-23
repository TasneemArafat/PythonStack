from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    context = {
        "all_dojos":dojos_obj(),
    }
    return render(request,'index.html',context)

def createdojo(request):
    if request.method == "POST":
        create_dojo(request.POST)
    return redirect('/')

def createninja(request):
    if request.method == "POST":
        create_ninja(request.POST)
    return redirect('/')

def delete(request):
    delete_dojo(request.GET['DeleteButton'])
    return redirect('/')