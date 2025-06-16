from django.shortcuts import render, redirect,get_object_or_404
from .models import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        Book.objects.create(
        title = request.POST.get('title'),
        desc = request.POST.get('desc'),
        )
        return redirect('/')
    context = {
        'books' : Book.objects.all(), 
    }
    return render(request,'index.html',context)


def author(request):
    if request.method == 'POST':
            Authors.objects.create(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            notes = request.POST.get('notes'),
            )
            return redirect('authors/')
    context = {
        'authors' : Authors.objects.all(), 
    }
    return render(request,'authors.html',context)



def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    all_authors = Authors.objects.all()

    if request.method == 'POST':
        author_id = request.POST.get('author')
        if author_id:
            author = Authors.objects.get(id=author_id)
            book.authors.add(author) 
            return redirect('book_detail', book_id=book.id)

    context = {
        'book': book,
        'all_authors': all_authors,
    }
    return render(request, 'books.html', context)

def author_detail(request, author_id):
    author = get_object_or_404(Authors, id=author_id)
    all_books = Book.objects.all()

    if request.method == 'POST':
        book_id = request.POST.get('book')
        if book_id:
            book = Book.objects.get(id=book_id)
            book.authors.add(author)
            return redirect('author_detail', author_id=author_id)

    context = {
        'author': author,       
        'books': all_books,
    }
    return render(request, 'all_authors.html', context)