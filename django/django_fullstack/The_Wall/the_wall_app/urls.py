from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('wall',views.welcome),
    path('logout',views.logout),
    path('login',views.login),
    path('add_message',views.add_message),
    path('add_comment',views.add_comment),
    path('delete_comment',views.delete_comment),
    path('delete_message',views.delete_message),
]
