from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.
def login_page(request):
    return render(request,'login.html')



def register(request):
    if request.method == 'POST':
        errors = User.object.validate_register(request.POST)
        if len(errors)>0:
            for key , value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            user = createUser(request.POST)
            request.session['user'] = user.id
            return redirect ('dashboard')
    else:
        return redirect('login')
    
def login(request):
    if request.method == 'POST':
        errors = User.object.validate_login(request.POST)
        if len(errors)>0:
            for key , value in errors.items():
                messages.error(request,value)
            return redirect('login')
        else:
            user = login_user(request.POST)
            if user:
                request.session['user'] = user.id
                return redirect('dashboard')
            else:
                messages.error(request,"Invalid email or password")
                return redirect('login')
    return redirect('/')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('login')

def dashboard(request):
    if 'user' in request.session:
        user = User.object.get(id=request.session['user'])
        project = Project.objects.all()
        context = {
            'user' : user,
            'project' :project,
        }
        return render(request,'dashboard.html',context)
    return redirect('login')




def createProject(request):
    if request.method == 'POST':
        errors = Project.objects.validate_project(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('createproject')
        else:
            project = create_Project(request.POST, request.session['user'])
            return redirect('projectDetails', project_id=project.id)
    return redirect('login')




def Project_page(request):
    if 'user' in request.session:
        user = User.object.get(id=request.session['user'])
        context={
            'user':user
        }
        return render(request,'createProject.html',context)
    else:
        return redirect('login')
    


def projectDetails(request, project_id):
    if 'user' not in request.session:
        return redirect('login')

    project = Project.objects.get(id=project_id)
    user = User.object.get(id=request.session['user'])

    context = {
        'project': project,
        'user': user,
        'owner': project.project_owner.id == user.id,
        'team_members': project.team.all(),
    }
    return render(request, 'projectDetails.html', context)


def editProject(request, project_id):
    if 'user' not in request.session:
        return redirect('login')

    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        project.name = request.POST['name']
        project.description = request.POST['description']
        project.start_date = request.POST['start_date']
        project.end_date = request.POST['end_date']
        project.save()
        return redirect('projectDetails', project_id=project.id)

    context = {
        'project': project
    }
    return render(request, 'edit_project.html', context)



def deleteProject(request, project_id):
    if 'user' not in request.session:
        return redirect('login')
    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect('dashboard')


def joinProject(request, project_id):
    if 'user' not in request.session:
        return redirect('login')
    
    user = User.object.get(id=request.session['user'])
    project = Project.objects.get(id=project_id)
    project.team.add(user)
    return redirect('dashboard')


def separateProject(request, project_id):
    if 'user' not in request.session:
        return redirect('login')
    
    user = User.object.get(id=request.session['user'])
    project = Project.objects.get(id=project_id)
    project.team.remove(user)
    return redirect('dashboard')