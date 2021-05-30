from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register',views.register),
    path('books',views.books),
    path('login',views.login),
    path('logout',views.logout),
    path('books/add_fav_book',views.add_fav_book),
    path('books/<int:book_id>',views.show_book),
    path('books/<int:book_id>/update',views.update_book),
    path('books/<int:book_id>/delete',views.delete_book),
    path('books/<int:book_id>/remove_from_fav',views.remove_from_fav),
    path('books/<int:book_id>/add_to_fav',views.add_to_fav),
]
