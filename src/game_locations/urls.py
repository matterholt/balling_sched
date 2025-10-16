from django.urls import path
from .views import (
    VenueListView,
    VenueCreatePage,
    VenueEditPage,
    VenueDetailPage,
    VenueDeletePage,
)

urlpatterns = [
    path("", VenueListView.as_view(), name="locations_list"),
    path("create", VenueCreatePage.as_view(), name="create_location"),
    path("<int:pk>/details", VenueDetailPage.as_view(), name="detail_location"),
    path("<int:pk>/edit", VenueEditPage.as_view(), name="edit_location"),
    path("<int:pk>/delete", VenueDeletePage.as_view(), name="delete_location"),
]
