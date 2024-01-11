from django.db import models

# Create your models here.


class ToDoList(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=300)
    to_do_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


