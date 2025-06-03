from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def create_user(request):
    name_from_form = request.POST['name']
    local_from_form = request.POST['local']
    language_from_form = request.POST['lang']
    comment_from_form = request.POST['comment']
    context = {
        "name":name_from_form,
        "local":local_from_form,
        "language": language_from_form,
        "comment": comment_from_form
    }
    return render(request,'result.html',context)