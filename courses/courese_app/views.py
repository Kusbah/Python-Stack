from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        errors = Coureses.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key , value in errors.items():
                messages.error(request,value)
            context = {
        'coures': Coureses.objects.all(),
        'old_data': request.POST
        }
            return render(request, 'index.html', context)
        else:
            Coureses.objects.create(
                name = request.POST.get('name'),
                description = request.POST.get('description')
            )
            return redirect('home')
        
    context = {
        'coures' : Coureses.objects.all()
    }
    return render(request,'index.html',context)


def confirm(request,id):
    course = get_object_or_404(Coureses,id=id)
    context = {
        'coures': course
    }
    return render(request,'confirm.html',context)


def remove(request,id):
    course = get_object_or_404(Coureses,id=id)
    course.delete()
    return redirect('home')