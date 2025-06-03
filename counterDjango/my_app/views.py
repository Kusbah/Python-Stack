from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
        request.session['counter'] =1
        return render(request,'index.html')
    return render(request,'index.html')

def delete(request):
    del request.session['counter']
    return render(request,'index.html')