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

            post_data = dict(product_id=Product.objects.get(id=int(request.POST.get('product'))) if request.POST.get('product') else None,
                             count=int(request.POST.get('count')) if request.POST.get('count') else None,
                             date=datetime.strptime(request.POST.get('date'), '%Y-%m-%d') if request.POST.get('date') else None,
                             status=Status.object.get(id=request.POST.get('status')) if request.POST.get('status') else None,
                             note=request.POST.get('note') if request.POST.get('note') else None)
            values_for_update = {k: v for k, v in post_data.items() if v is not None}

            if len(values_for_update.keys()) > 0:

                order, created = ActualOrder.objects.update_or_create(id=request.POST.get('id'),
                                                                      defaults=values_for_update)
                res['scs'] = True
                res['msg'] = f'Новый заказ №{order.id} добавлен' if created else f'Заказ №{order.id} обновлен'
                res['order'] = {'id': order.id,
                                'product': order.product_id.name,
                                'count': str(order.count)+' шт.',
                                'date': order.date.strftime('%d.%m.%Y'),
                                'status': {
                                    'name': order.status.name,
                                    'class': order.status.style_class,
                                    'icon': order.status.icon
                                },
                                'note': order.note}

            else:
                res['scs'] = True
                res['msg'] = 'Ничего не произошло'
        # elif action == 'edit':

        elif action == 'delete':
            ActualOrder.objects.filter(id=request.POST.get('id')).delete()
            res['msg'] = f'Актуальный заказ №{request.POST.get("id")} удален'
            res['scs'] = True
        return JsonResponse(res)
    else:
        return HttpResponseNotAllowed('<h2>Ошибка</h2>')




def db_szi(request):
    pass



