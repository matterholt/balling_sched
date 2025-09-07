
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import Venue
from ..forms import VenueForm

class VenueListView(ListView):
  model = Venue
  template_name = "locations/locations_list.html"
  context_object_name = "locations"

class VenueCreateView(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = "locations/partials/location_form.html"
    success_url = reverse_lazy("venue_list")

class VenueCreatePage(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = "locations/partials/new_location_page.html"
    success_url = reverse_lazy("locations_list")
