from django.shortcuts import render
from django.http import *
from .forms import UserForm, AddOrder
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html", {'form': UserForm()})


def actual(request):
    if request.method == 'GET':
        return render(request, 'actual.html', {'form': AddOrder(), 'orders': ActualOrder.object.in_bulk()})
    elif request.method == 'POST':
        return 'ok'
    else:
        return HttpResponseNotAllowed('Ошибка')
