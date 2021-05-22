from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('process_money',views.money),
    path('clear',views.clear),
    path('<str:place>',views.money_place),
]