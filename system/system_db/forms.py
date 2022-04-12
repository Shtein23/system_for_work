from django import forms


class  UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента')
    age = forms.IntegerField(label='Возраст')
