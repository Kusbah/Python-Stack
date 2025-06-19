from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request,'index.html')


def registration(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('home')
        else:
            pw_hash = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = pw_hash
            )
            request.session['user_id'] = user.id
            context = {
                'user' : user
            }
            
            return render(request,'well.html',context)
    else:
        return redirect('home')
    
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password =request.POST['password']
        user = User.objects.filter(email=email).first()
        if user:
            if bcrypt.checkpw(password.encode(),user.password.encode()):
                request.session['user_id'] = user.id
                context = {
                'user' : user
            }

                return render(request, 'well.html',context)
            else:
                messages.error(request, "Incorrect password")
        else:
            messages.error(request, "Email not found")
    return redirect('home')

def logout(request):
    request.session.flush() 
    return redirect('home') 


def message_wall(request):
    if 'user_id' not in request.session:
        return redirect('home') 
    user = User.objects.get(id=request.session['user_id'])
    all_messages = Message.objects.all().order_by('-created_at')
    context = {
        'messages': all_messages,
        'user': user
    }
    return render(request, 'well.html', context)

def post_message(request):
    if request.method == 'POST':
        if 'user_id' not in request.session:
            return redirect('home')

        try:
            user = User.objects.get(id=request.session['user_id'])
            Message.objects.create(
                user_id=user,
                message=request.POST['message']
            )
        except User.DoesNotExist:
            request.session.flush()  # إفراغ الجلسة
            return redirect('home')

    return redirect('well')