from django.shortcuts import render

def form_page(request):
    return render(request,'form.html')

def result_page(request):
    form_name = request.POST['name']
    form_location = request.POST['location']
    form_language = request.POST['language']
    form_comments = request.POST['comment']
    form_gender = request.POST['gender']
    form_courses = request.POST.getlist('courses')

    context = {
        'name' : form_name,
        'location' : form_location,
        'language' : form_language,
        'comments' : form_comments,
        'gender' : form_gender,
        'courses':form_courses,
    }

    return render(request,'info.html',context)