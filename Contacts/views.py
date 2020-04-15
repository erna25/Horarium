from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'Contacts/homepage.html', )
# Create your views here.
