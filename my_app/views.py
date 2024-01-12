from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateToDoList
# from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return HttpResponse("Hello World")


def home(request):
    return render(request, "my_app/base.html", {})


def lists(request):
    # to_do_lists = ToDoList.objects.all()
    to_do_lists = request.user.todolist.all()
    # print("request")
    if request.method == "POST":
        # print("post request")
        # print(request.POST)
        if request.POST.get("add"):
            for to_do_list in to_do_lists:
                item_name = f"new{to_do_list.id}"
                new_item = request.POST.get(item_name)
                if new_item:
                    to_do_list.item_set.create(name=new_item)
                    to_do_list.save()

        elif request.POST.get("save"):
            for to_do_list in to_do_lists:
                for item in to_do_list.item_set.all():
                    checkbox_name = f"c{item.id}"
                    if request.POST.get(checkbox_name):
                        # print(f"{checkbox_name} found on")
                        item.completed = True
                    else:
                        # print(f"{checkbox_name} not found")
                        item.completed = False
                    item.save()

    return render(request, "my_app/list.html", {"lists": to_do_lists})


def get_list(request, name):
    # ls = ToDoList.objects.filter(name=name)
    ls = User.todolist_set.objects.filter(name=name)
    return render(request, "my_app/list.html", {"lists": ls})


def create(request):
    if request.method == "POST":
        form = CreateToDoList(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            ls = ToDoList(name=n)
            ls.save()
            request.user.todolist.add(ls)
    # else:
    #     # ls = ToDoList.objects.all()
    #     form = CreateToDoList()
    #     # return render(request, "my_app/create.html", {"form": form, "lists": ls})
    #     return render(request, "my_app/create.html", {"form": form})
    new_form = CreateToDoList()
    return render(request, "my_app/create.html", {"form": new_form})
