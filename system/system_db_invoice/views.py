from django.shortcuts import render
from django.http import *
from .forms import UserForm

# Create your views here.


def index(request):
    return render(request, "index.html", {'form': UserForm()})
