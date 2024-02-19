from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('hello', views.hello_world),
    path('home', views.home_page),
    path('task', views.task_page),
    path('analytics', views.analytics_page),
    path('all-analytics', views.all_analytics)
]