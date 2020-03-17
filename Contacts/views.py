from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Контактная информация")
# Create your views here.
