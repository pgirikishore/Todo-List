from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path('<str:tile_item>', views.items, name='items'),
    path(r'<str:tile_id>', views.delete_tile, name='delete_tile'),
    path(r'<str:key>/<str:item>', views.delete_item, name='delete_item'),
]