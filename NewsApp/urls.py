from django.urls import path
from NewsApp import views

urlpatterns = [
    path('', views.home,name='home' ),
]
