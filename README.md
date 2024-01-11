# myfirstdjproject

Django - ToDoList

# If faced even while creating superuser like: 
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