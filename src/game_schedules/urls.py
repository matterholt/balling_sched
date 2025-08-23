from django.urls import path
from .views import VenueListView
# VenueCreateView, VenueUpdateView, VenueDeleteView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('locations', VenueListView.as_view(), name='locations_list'),
    path("locations/upload-csv/", views.upload_csv, name="upload_csv"),
    path("<str:year>", views.year, name="year"),

]
