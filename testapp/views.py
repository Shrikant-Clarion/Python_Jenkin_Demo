from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return HttpResponse("Hello, world. Jenkin Integration with Github successfully done.")
    #return HttpResponse("Jenkin Integration with Github successfully done.")
