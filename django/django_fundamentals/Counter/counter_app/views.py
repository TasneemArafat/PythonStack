from django.shortcuts import render,redirect

def index(request):
    if 'counter' not in request.session:
        request.session['counter']=1
    if 'counter2' not in request.session:
        request.session['counter2']=1

    if request.session['check1']!=0 and request.session['check2']!=0:
        print(request.session['check1'])
        print(request.session['check1'])
        if 'counter2' not in request.session:
            request.session['counter2'] = 1
        else:
            request.session['counter2'] +=1
            request.session['check1']=1
            request.session['check2']=1
    return render(request,'index.html')

def destroy(request):
    del request.session['counter2']
    del request.session['counter']
    return redirect('/')

    
def counter (request):
    request.session['counter']+=2
    request.session['check1'] = 0
    return redirect('/')

def numinc (request):
    if request.method == 'POST':
        request.session['counter']+= int(request.POST['inc'])
    request.session['check2'] = 0
    return redirect( '/')
