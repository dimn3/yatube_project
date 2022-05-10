from . import views
from django.urls import path


urlpatterns = [
    #главная
    path('', views.index),
    #группы
    path('group/<slug:slug>/', views.group_posts)
] 
