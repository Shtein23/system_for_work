import datetime
from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __repr__(self):
        return f'<Пользователь {self.name} {self.surname}>'


class Product(models.Model):
    name = models.CharField(max_length=128)
    objects = models.Manager()

    def __repr__(self):
        return f'<Изделие {self.name}>'


class Status(models.Model):
    name = models.CharField(max_length=30)
    style_class = models.TextField()
    object = models.Manager()

    def __repr__(self):
        return f'<Статус {self.name}>'


class Label(models.Model):
    name = models.CharField(max_length=30)
    style_class = models.TextField()
    object = models.Manager()


class ActualOrder(models.Model):
    product_id = models.ForeignKey(Product,
                                   on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)
    # label = models.ForeignKey(Label, on_delete=models.DO_NOTHING, default=None)
    date = models.DateField()
    status = models.ForeignKey(Status,
                               on_delete=models.DO_NOTHING)
    note = models.TextField(default='')
    objects = models.Manager()

    def __repr__(self):
        return f'<Актуальный заказ №{self.id}>'


