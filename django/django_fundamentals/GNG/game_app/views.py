from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
import random

def home(request):
    if 'color' not in request.session:
        request.session['color'] = "blank"
    if 'number' not in request.session:
        request.session['number'] = random.randint(1,100)
    if 'counter' not in request.session:
        request.session['counter'] = 0
    print(request.session['number'])
    return render(request, 'home.html')

def result(request):
    num = request.session['guessnum']
    if num > request.session['number']:
        request.session['guess']="Too High"
        request.session['color']="red"
    elif num < request.session['number']:
        request.session['guess']="Too Low"
        request.session['color']="red"
    elif num == request.session['number']:
        request.session['guess']="You Got it"
        request.session['color']="green"
    return redirect('/')

def restart(request):
    request.session.clear()
    return redirect('/')
    
def loser(request):
    request.session['color'] = "blue"
    request.session['guess'] = "YOU LOSE" 
    return redirect('/') 

def guess(request):
    request.session['guessnum']=int(request.POST['guess'])
    if request.session['counter'] != 5:
        request.session['counter'] += 1
    else:
        return redirect('/loser')
    return redirect('/result')


    