from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('dojos',views.createdojo),
    path('ninjas',views.createninja),
    path('deletion',views.delete)
]