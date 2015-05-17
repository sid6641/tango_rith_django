from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello rango! Index page")

def about(request):
    return HttpResponse("Rango says here is the about page.")