from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Create your views here.
def index(response):
    return HttpResponse("working........")

def start(response):
    return HttpResponse("start area.")