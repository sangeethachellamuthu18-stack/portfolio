from django.contrib import admin
from django.urls import path
from resume import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume'),

]