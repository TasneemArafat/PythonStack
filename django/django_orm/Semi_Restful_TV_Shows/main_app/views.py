from django.http.request import HttpRequest
from django.shortcuts import render,HttpResponse,redirect
from . import models

# Create your views here.
def redirect_to_shows(request):
    return redirect('/shows')
    
def shows(request):
    context = {
        'all_shows':models.all_shows()
    }
    return render(request,'shows.html',context)

def new_show(request):
    return render(request,"new_show.html")

def add_show(request):
    if request.method == 'POST':
        title = request.POST['title']
        network = request.POST['network']
        release_date = request.POST['rd']
        desc = request.POST['desc']
        id = models.add_shows(title,network,release_date,desc)
        value = '/shows/'+str(id)
        return redirect(value)
    return redirect('/shows')

def view_show(request,id):
    show = models.get_show(id)
    context = {
        'show' : show
    }
    return render(request,'view_show.html',context)

def edit_show(request,id):
    show = models.get_show(id)
    context = {
        'show' : show
    }
    return render(request,'edit_show.html',context)

def update_show(request,id):
    show = models.get_show(id)
    models.update_show(id,request.POST['title'],request.POST['network'],request.POST['rd'],request.POST['desc'])
    value = '/shows/'+str(id)
    return redirect(value)

def delete_show(request,id):
    models.delete_show(id)
    return redirect('/shows')
