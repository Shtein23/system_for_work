from django.shortcuts import render
from django.http import *
from .forms import UserForm, AddOrder
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html", {'form': UserForm()})


def actual(request):
    if request.method == 'GET':
        return render(request, 'actual.html', {'form': AddOrder(),
                                               'orders': ActualOrder.objects.all(),
                                               'status': Status.object.all()})
    elif request.method == 'POST':
        new_order = ActualOrder(product_id=Product.object.get(id=int(request.POST.get('product'))),
                                count=request.POST.get('count'),
                                date=request.POST.get('date'),
                                status=Status.object.get(id=1),
                                note=request.POST.get('note') + '\n')
        new_order.save()
        return JsonResponse({'res': 'ok'})
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        print(request.POST.get('id'))
        ActualOrder.objects.filter(id=request.POST.get('id')).delete()
    else:
        return HttpResponseNotAllowed('<h2>Ошибка</h2>')
