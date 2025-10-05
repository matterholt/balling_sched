from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from ..models import Venue
from ..forms import VenueForm


class VenueBaseView(View):
    model = Venue
    fields = "__all__"
    success_url = reverse_lazy("locations_list")


class VenueListView(VenueBaseView, ListView):
    template_name = "locations/locations.html"
    context_object_name = "locations"


class VenueDetailPage(VenueBaseView, DetailView):
    template_name = "locations/subpages/detail_location.html"


class VenueCreatePage(VenueBaseView, CreateView):
    template_name = "locations/subpages/add_location.html"


class VenueEditPage(VenueBaseView, UpdateView):
    template_name = "locations/subpages/edit_location.html"


class VenueDeletePage(VenueBaseView, DeleteView):
    template_name = "locations/subpages/delete_location.html"
