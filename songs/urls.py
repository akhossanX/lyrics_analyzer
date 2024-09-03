from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_song/', views.add_song, name='add_song'),
]