from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('add_book',views.add_book),
    path('books/<int:id>',views.view_book),
    path('authors',views.show_authors),
    path('add_author',views.add_author),
    path('author/<int:id>',views.view_author),
    path('select_author', views.select_author),
    path('select_book',views.select_book)
]