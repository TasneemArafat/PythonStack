from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('user_info',views.add_user)
]