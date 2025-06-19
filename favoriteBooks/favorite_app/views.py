from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from . import models
# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validate_register(request.POST)
        if len(errors)>0:
            for key , value in errors.items():
                messages.error(request,value)
            return redirect('login')
        else:
            user = models.createUser(request.POST)
            request.session['user'] = user.id
            return redirect('books')
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        errors = User.objects.validate_login(request.POST)
        if len(errors)>0:
            for key , value in errors.items():
                messages.error(request,value)
            return redirect('login')
        else:
            user = models.login_user(request.POST)
            if user:
                request.session['user'] = user.id
                return redirect('books')
            else:
                messages.error(request,"Invalid email or password")
                return redirect('login')
    return redirect('/')


def books(request):
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        context = {
            'user': user,
            'all_books': Book.objects.all()
        }
        return render(request, 'books.html', context)
    return redirect('login')

def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('login')

def addBook(request):
    if request.method == 'POST':
        errors = Book.objects.validate_book(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('books')
        else:
            book = models.createBook(request.POST,request.session['user'])
            return redirect('books')
    redirect('/books')

def view_book(request, id):
    if 'user' not in request.session:
        return redirect('login')

    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['user'])

    context = {
        'book': book,
        'user': user,
        'is_uploader': book.uploaded_by.id == user.id,
        'favorites': book.users_who_like.all()
    }
    return render(request, 'book_detail.html', context)
    

def update_book(request, id):
    if request.method == 'POST':
        if 'user' not in request.session:
            return redirect('login')
        
        book = Book.objects.get(id=id)
        user = User.objects.get(id=request.session['user'])

        if book.uploaded_by.id != user.id:
            messages.error(request, "You are not allowed to update this book.")
            return redirect('view_book_user')

        book.title = request.POST['title']
        book.desc = request.POST['description']
        book.save()
        return redirect('view_book', id=id)
    
def delete_book(request, id):
    if request.method == 'POST':
        if 'user' not in request.session:
            return redirect('login')       
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('books')
    
def view_book_user(request):
    if 'user' not in request.session:
        return redirect('login')

    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['user'])

    context = {
        'book': book,
        'user': user,
        'is_uploader': book.uploaded_by.id == user.id,
        'favorites': book.users_who_like.all()
    }
    render(request,'book_detail_user.html')

def favorite_book(request, id):
    if 'user' not in request.session:
        return redirect('login')

    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['user'])
    book.users_who_like.add(user)
    return redirect('view_book', id=id)


def unfavorite_book(request, id):
    if 'user' not in request.session:
        return redirect('login')

    book = Book.objects.get(id=id)
    user = User.objects.get(id=request.session['user'])
    book.users_who_like.remove(user)
    return redirect('view_book', id=id)
