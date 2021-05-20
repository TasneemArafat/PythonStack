from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('guess',views.guess),
    path('result',views.result),
    path('restart',views.restart),
    path('loser',views.loser),
]