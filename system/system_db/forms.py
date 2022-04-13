from django import forms
from .models import *


class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента')
    age = forms.IntegerField(label='Возраст')


class AddOrder(forms.Form):
    product = forms.Select()
    count = forms.IntegerField(label='Количество', min_value=1, max_value=1000)
    label = forms.Select()
