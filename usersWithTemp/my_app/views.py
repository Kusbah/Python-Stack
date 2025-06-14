from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method == 'POST':
        User.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            age=request.POST.get('age')
        )
        return redirect('/')
    context={
        'users':User.objects.all()
    }
    return render(request,'index.html',context)