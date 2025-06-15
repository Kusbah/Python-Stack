from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        Dojo.objects.create(
            name = request.POST.get('name'),
            city = request.POST.get('city'),
            state = request.POST.get('state')
        )
        # dojo_id = request.POST.get('dojo')
        # dojo = Dojo.objects.get(id=dojo_id)
        Ninja.objects.create(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            dojo=Dojo
            
        )
        return redirect('/')
    context = {
        "ninja":Ninja.objects.all(),
        "dojos": Dojo.objects.all()
    }
    return render(request,"index.html",context)