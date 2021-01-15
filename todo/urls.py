from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index),
    path('index/', views.index, name='index'),
    path(r'<item_id>', views.delete_item, name='delete_item'),
]