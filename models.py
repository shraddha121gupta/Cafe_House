from django.db import models

# Create your models here.
from django.db.models import IntegerField


class cafe_menu(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True)
    price = models.IntegerField()
    def __str__(self):
        return self.name


class menu_list(models.Model):
    category = models.ForeignKey(cafe_menu, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(null=True)
    price = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class todays(models.Model):
    combo_name = models.CharField(max_length=30)
    name1 = models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)
    name3 = models.CharField(max_length=30)
    image = models.ImageField(null=True)
    price = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True)
    def __str__(self):
        return self.combo_name









