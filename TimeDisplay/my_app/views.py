from django.shortcuts import render
from django.http import HttpResponse
from time import gmtime, strftime
# Create your views here.


        
def index(request):
    context = {
        "data": strftime(" %B %d, %Y ", gmtime()),
        "time": strftime("%H:%M %p",gmtime())
    }
    return render(request,'index.html', context)