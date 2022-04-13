from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=128)
    object = models.Manager()


class Status(models.Model):
    name = models.CharField(max_length=30)
    style_class = models.TextField()


class Label(models.Model):
    name = models.CharField(max_length=30)
    style_class = models.TextField()
    object = models.Manager()


class ActualOrder(models.Model):
    number = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)
    # label = models.ForeignKey(Label, on_delete=models.DO_NOTHING, default=None)
    date = models.TextField(default='')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    object = models.Manager()


