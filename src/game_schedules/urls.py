from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("locations", views.location, name="locations"),
    path("<str:year>", views.year, name="year"),

]
