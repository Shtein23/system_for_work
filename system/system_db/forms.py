from django import forms
from .models import *


class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента')
    age = forms.IntegerField(label='Возраст')


class AddOrder(forms.Form):
    product = forms.ChoiceField(label='Выберать изделие', choices=tuple((x.id, x.name) for x in Product.object.all()))
    count = forms.IntegerField(label='Количество', min_value=1, max_value=1000)
    # label = forms.ChoiceField(choices=tuple((x.id, x.name) for x in Label.object.all()))
    date = forms.CharField(label='Необходимый срок')
