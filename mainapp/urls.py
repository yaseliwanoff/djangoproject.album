from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('photos/', views.posts, name='photos'),
]
