from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def home(request):
    return render(request, "my_app/base.html", {})


def lists(request):
    ls = ToDoList.objects.all()
    return render(request, "my_app/list.html", {"lists": ls})


def get_list(request, name):
    ls = ToDoList.objects.filter(name=name)
    return render(request, "my_app/list.html", {"lists": ls})
