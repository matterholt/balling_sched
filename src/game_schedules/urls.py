from django.urls import path
from .views.base import ScheduledGames
from .views.venues import VenueListView
from .views.api import VenueDeleteHTMX
from .views.base import spreadsheet_upload
# VenueCreateView, VenueUpdateView, VenueDeleteView


urlpatterns = [
    path("", ScheduledGames.as_view(), name="index"),
    path("locations", VenueListView.as_view(), name="locations_list"),
    path("locations/spreadsheet_upload/", spreadsheet_upload, name="spreadsheet_upload"),


    path("action/delete/<int:pk>", VenueDeleteHTMX.as_view(), name="delete_location_entry")
]
