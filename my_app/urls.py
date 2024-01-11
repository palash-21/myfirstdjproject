from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="hello world"),
    path('home/', views.home, name="home"),
    path('list/', views.lists, name="lists"),
    path('list/<str:name>/', views.get_list, name="get_list")
]
