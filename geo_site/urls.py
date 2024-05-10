from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.test, name="test"),
    path("learn/match", views.learn_match, name="learn"),
    path("hoorah", views.hoorah, name="learn"),
    path("learn/5", views.learn_end, name="learn"),
    path("learn/", views.learn_start, name="learn"),
    path("learn/<int:number>", views.learn, name="learn")
]
