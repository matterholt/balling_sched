from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:year>", views.year, name="year"),

]
