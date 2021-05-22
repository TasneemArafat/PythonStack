from django.http.response import HttpResponse
from time import gmtime, strftime
from django.shortcuts import render,redirect
import random

# Create your views here.
def home(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'activity' not in request.session:
        request.session['activity'] = []
    context = {
        'earning' : request.session['activity'],
        'gold_amount' : request.session['count']
    }
    return render(request,"home.html",context)


def money(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    value = 0
    if request.method == 'POST':
        if request.POST['gold'] == "farm":
            value = random.randint(10,20)
        elif request.POST['gold'] == 'cave':
            value = random.randint(5,10)
        elif request.POST['gold'] == 'house':
            value = random.randint(2,5)
        elif request.POST['gold'] == 'casino':
            value = random.randint(-50,50)
        if value < 0:
            request.session['activity'].append(f"you entered a {request.POST['gold']} and lost {value} gold .. ouch ..")
            request.session['color'] = "red"
        elif value > 0:
            request.session['activity'].append(f"Earned {value} golds from the {request.POST['gold']}!")
            request.session['color'] = "green"
    request.session['count'] += value
    print(value)
    print(request.session['count'])

    return redirect('/')

def money_place(request,place):
    if 'count' not in request.session:
        request.session['count'] = 0
    value = 0
    if request.method == 'GET':
        if place == "farm":
            value = random.randint(10,20)
        elif place == 'cave':
            value = random.randint(5,10)
        elif place == 'house':
            value = random.randint(2,5)
        elif place == 'casino':
            value = random.randint(-50,50)
        else:
            return HttpResponse("Place does not exist")
        if value < 0:
            request.session['activity'].append(f"you entered a {place} and lost {value} gold .. ouch .. ")
            request.session['color'] = "red"
        elif value > 0:
            request.session['activity'].append(f"Earned {value} golds from the {place}!")
            request.session['color'] = "green"
    request.session['count'] += value
    print(value)
    print(request.session['count'])
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')
    
    