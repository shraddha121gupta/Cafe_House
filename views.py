from django.shortcuts import render
from django import http
from .models import *
def home(request):
    return render(request, "homes.html")
# Create your views here.
def menus(request):
    data = cafe_menu.objects.all()
    Dict = {"food" : data}
    return render(request, "menu.html", Dict)
def locations(request):
    return render(request, "location.html")
def menu_lists(request, num):
    data = cafe_menu.objects.get(id=num)
    list_menu = menu_list.objects.filter(category=data)
    Dict = {"food": list_menu, "names": data}
    return render(request, "menu_list.html", Dict)
def todays_meal(request):
    data = todays.objects.all()
    Dict = {"food": data}
    return render(request, "today.html", Dict)


