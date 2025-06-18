from django.shortcuts import render,redirect,get_object_or_404
import bcrypt
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'success.html')

def register(request):
    if request.method == 'POST':
        errors = Users.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key , value in errors.items():
                messages.error(request,value)
            return redirect('home')
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

            user = Users.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash
            )
            context = {
                'user' : user
            }

            return render(request, 'success.html',context)
    else:
        return redirect('/')
    


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = Users.objects.filter(email=email).first()

        if user:
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                request.session['user_id'] = user.id
                context = {
                'user' : user
            }

                return render(request, 'success.html',context)
            else:
                messages.error(request, "Incorrect password")
        else:
            messages.error(request, "Email not found")

    return redirect('home')

def logout(request):
    request.session.flush() 
    return redirect('home') 