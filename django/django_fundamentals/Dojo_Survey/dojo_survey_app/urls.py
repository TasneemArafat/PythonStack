from django.urls import path
from . import views

urlpatterns = [
    path('', views.form_page),
    path('result',views.result_page),
]