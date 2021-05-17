from django.urls import path 
from . import views

urlpatterns = [
    path('',views.displaytime),
    path('time_display',views.displaytime),
]