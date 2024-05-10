from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("learn/5", views.learn_end, name="learn"),
    path("learn/", views.learn_start, name="learn"),
    path("learn/<int:number>", views.learn, name="learn")
]
