from django.urls import path
from .views.base import ScheduledGames
from .views.venues import VenueListView,VenueCreatePage,VenueEditPage,VenueDetailPage,VenueDeletePage
from .views.api import VenueDeleteHTMX
from .views.base import spreadsheet_upload
# , VenueUpdateView, VenueDeleteView


urlpatterns = [
    path("", ScheduledGames.as_view(), name="index"),
    path("locations", VenueListView.as_view(), name="locations_list"),
    path("locations/create", VenueCreatePage.as_view(), name="create_location"),
    path("locations/<int:pk>/details", VenueDetailPage.as_view(), name="detail_location"),
    path("locations/<int:pk>/edit", VenueEditPage.as_view(), name="edit_location"),
    path("locations/<int:pk>/delete", VenueDeletePage.as_view(), name="delete_location"),

    path("locations/spreadsheet_upload/", spreadsheet_upload, name="spreadsheet_upload"),
    # HTX
    path("api/locations/<int:pk>/details", VenueDeleteHTMX.as_view(), name="details_location_entry"),
    path("api/locations/<int:pk>/delete", VenueDeleteHTMX.as_view(), name="delete_location_entry"),
    path("api/locations/<int:pk>/edit", VenueDeleteHTMX.as_view(), name="edit_location_entry"),
]
