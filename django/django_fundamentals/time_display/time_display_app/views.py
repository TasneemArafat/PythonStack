from django.shortcuts import render
from time import gmtime, strftime
import time



def displaytime(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time":time.strftime("%H:%M:%S %p",time.localtime()),
    }
    return render(request,'index.html', context)
