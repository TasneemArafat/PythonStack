from django.urls import path
from . import views

urlpatterns = [
    path('',views.redirect_to_shows),
    path('shows',views.shows),
    path('shows/new',views.new_show),
    path('shows/create',views.add_show),
    path('shows/<int:id>',views.view_show),
    path('shows/<int:id>/edit',views.edit_show),
    path('shows/<int:id>/update',views.update_show),
    path('shows/<int:id>/destroy',views.delete_show),
]