from django.shortcuts import render,redirect
from random import randint
# Create your views here.

def index(request):
    if 'number' not in request.session:
        request.session['number'] = randint(1, 100)
        request.session['message'] = ''
    return render(request,'index.html',{
    'message': request.session.get('message', '')})

    
def guess(request):
    number_from_form = int(request.POST['num'])

    if number_from_form > request.session['number']:
        request.session['message'] = 'Too high!'
    elif number_from_form < request.session['number']:
        request.session['message'] = 'Too low!'
    else:
        request.session['message'] = f'Correct! The number was {request.session['number']}'
    return redirect('/')

def playAginie(request):
    request.session.clear()
    return redirect('/')



 

