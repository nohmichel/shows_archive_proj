from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('shows/new', views.index, name="new_show"),
    path('shows/create', views.create_new),
    path('shows/<int:show_id>', views.show_bio, name="show_bio"),
    path('shows', views.shows, name="show_list"), 
    path('shows/<int:show_id>/edit', views.edit_show, name="edit_show"),
    path('shows/<int:show_id>/update', views.update_show, name="update_show"),
    path('shows/<int:show_id>/destroy', views.delete_show, name="delete_show")

    
    
]