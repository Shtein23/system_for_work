from django.shortcuts import render
from django.http import *
from .forms import UserForm, AddOrder
from .models import *
from datetime import datetime


# Create your views here.


def index(request):
    return render(request, "index.html", {'form': UserForm()})


def actual(request):
    if request.method == 'GET':
        return render(request, 'actual.html', {'form': AddOrder(),
                                               'orders': ActualOrder.objects.all(),
                                               'status': Status.object.all(),
                                               'main': 'actual'})
    elif request.method == 'POST':
        action = request.POST.get('action')
        res = {'scs': False, 'msg': 'Ошибка действия'}
        if action == 'add':
            new_order = ActualOrder(product_id=Product.object.get(id=int(request.POST.get('product'))),
                                    count=request.POST.get('count'),
                                    date=datetime.strptime(request.POST.get('date'), '%Y-%m-%d'),
                                    status=Status.object.get(id=1),
                                    note=request.POST.get('note') + '\n')
            new_order.save()
            res['msg'] = f'Новый заказ №{new_order.id} добавлен'
            res['scs'] = True

            res['order'] = {'id': new_order.id,
                            'product': new_order.product_id.name,
                            'count': new_order.count,
                            'date': new_order.date.strftime('%d.%m.%Y'),
                            'status': new_order.status.name,
                            'note': new_order.note}
        elif action == 'edit':
            pass
        elif action == 'delete':
            ActualOrder.objects.filter(id=request.POST.get('id')).delete()
            res['msg'] = f'Актуальный заказ №{request.POST.get("id")} удален'
            res['scs'] = True
        return JsonResponse(res)
    else:
        return HttpResponseNotAllowed('<h2>Ошибка</h2>')



