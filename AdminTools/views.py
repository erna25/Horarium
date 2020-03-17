from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Внесение изменений в расписание")
# Create your views here.
