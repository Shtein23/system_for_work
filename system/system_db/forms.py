from django import forms
from .models import *


class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента')
    age = forms.IntegerField(label='Возраст')


def prod():
    x = [(x.id, x.name) for x in Product.objects.all()]
    x.insert(0, ('0', 'Выбрать...'))
    return tuple(x)


class AddOrder(forms.Form):
    product = forms.ChoiceField(label='Выберать изделие',
                                choices=prod(),
                                widget=forms.Select(attrs={'class': 'form-select mb-2 js-chosen'}))
    count = forms.IntegerField(label='Количество',
                               min_value=1,
                               max_value=1000,
                               widget=forms.NumberInput(attrs={'class': 'form-control mb-2'}))
    # label = forms.ChoiceField(choices=tuple((x.id, x.name) for x in Label.object.all()))
    date = forms.DateField(label='Желаемая дата готовности',
                           widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-2'}),
                           initial=datetime.date.today().strftime('%Y-%m-%d'))
    note = forms.CharField(label='Примечание',
                           required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control mb-2'}))
    status = forms.IntegerField(widget=forms.HiddenInput, initial=1)


