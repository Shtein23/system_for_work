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

        if action == 'add' or action == 'edit':

            # old add orders func
            # new_order = ActualOrder(product_id=Product.objects.get(id=int(request.POST.get('product'))),
            #                         count=int(request.POST.get('count')),
            #                         date=datetime.strptime(request.POST.get('date'), '%Y-%m-%d'),
            #                         status=Status.object.get(id=request.POST.get('status')),
            #                         note=request.POST.get('note'))
            # new_order.save()
            # res['msg'] = f'Новый заказ №{new_order.id} добавлен'
            # res['scs'] = True

            post_data = dict(product_id=Product.objects.get(id=int(request.POST.get('product'))) or None,
                             count=int(request.POST.get('count')) or None,
                             date=datetime.strptime(request.POST.get('date'), '%Y-%m-%d') or None,
                             status=Status.object.get(id=request.POST.get('status')) or None,
                             note=request.POST.get('note') or None)
            values_for_update = {k: v for k, v in post_data.items() if v is not None}

            order, created = ActualOrder.objects.update_or_create(id=request.POST.get('id'),
                                                                  defaults=values_for_update)
            res['scs'] = True
            res['msg'] = f'Новый заказ №{order.id} добавлен' if created else f'Заказ №{order.id} обновлен'

        # elif action == 'edit':

        elif action == 'delete':
            ActualOrder.objects.filter(id=request.POST.get('id')).delete()
            res['msg'] = f'Актуальный заказ №{request.POST.get("id")} удален'
            res['scs'] = True
        return JsonResponse(res)
    else:
        return HttpResponseNotAllowed('<h2>Ошибка</h2>')



