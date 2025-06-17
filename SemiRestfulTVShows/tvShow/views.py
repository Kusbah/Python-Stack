from django.shortcuts import render ,redirect,get_object_or_404
from .models import *
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return render(request, 'index.html')
        else:
            new_show = Show.objects.create(
                title=request.POST.get('title'),
                network=request.POST.get('network'),
                release_date=request.POST.get('release_date'),
                description=request.POST.get('description'),
            )
            messages.success(request, "Show successfully created")
            return redirect('show_detail', id=new_show.id)

    return render(request, 'index.html')

def show_detail(request, id):
    show = get_object_or_404(Show, id=id)
    context = {
        'show': show
    }
    return render(request, 'show_detail.html', context)

def shows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request,'shows.html',context)

def delete_show(request, id):
    show = get_object_or_404(Show, id=id)
    show.delete()
    return redirect('show')


def edit_show(request, id):
    show = get_object_or_404(Show, id=id)
    
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        for key ,value in errors.items():
            messages.error(request,value)
            return render(request , 'edit_show.html')
        else:
            show.title = request.POST.get('title')
            show.network = request.POST.get('network')
            show.release_date = request.POST.get('release_date')
            show.description = request.POST.get('description')
            show.save()
            return redirect('show_detail', id=show.id)
    context = {
        'show' : show
    }
    
    return render(request, 'edit_show.html', context)
