from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("placeholder to display all the surveys created.")

def new(request):
    return HttpResponse("placeholder for users to add a new survey.")