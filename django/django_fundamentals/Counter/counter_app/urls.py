from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('destroy_session',views.destroy),
    path('counter', views.counter),
    path('numinc', views.numinc),
]
