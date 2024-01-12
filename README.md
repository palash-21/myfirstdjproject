# myfirstdjproject

Django - ToDoList

# If faced error while creating superuser like: 
    $ python manage.py createsuperuser
    Superuser creation skipped due to not running in a TTY. You can run manage.py createsuperuser in your project to create one manually.
    then use winpty
    winpty python manage.py createsuperuser
    username: admin
    email: admin@gmail.com
    psd: admin@123


# Connect with django python shell using :
    python manage.py shell
# Creating/adding item to a todolist using shell:
    python manage.py shell
    from my_app.models import ToDoList
    ls = ToDoList.objects.get(id=1)
    (or ls = ToDoList.objects.get(name='myToDoList')
    ls.item_set.create(name="do something")
    ls.save()

# ToDoList
![Model](https://github.com/palash-21/myfirstdjproject/blob/main/ToDoList.png)

# Admin Dashboard
![Model](https://github.com/palash-21/myfirstdjproject/blob/main/Admin.png)


# Forms in django 
    To add form in html, we just need to 
    add the form element with method & action,
    the submit button
    and use a {{form}} object for all the fields 
    # note : need to always use {% csrf_token %} inside the form element in django

# User Registration ,login, user-wise todolist
![Model](https://github.com/palash-21/myfirstdjproject/blob/main/Register.png)
![Model](https://github.com/palash-21/myfirstdjproject/blob/main/login.png)
