
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from ..models import Venue


class VenueListView(ListView):
  model = Venue
  template_name = "locations/locations_list.html"
  context_object_name = "locations"

# traditional
class VenueDelete (DeleteView):
  model = Venue
  template_name = "locations/venue_delete.html"
  # success_url = "/locations/"
  success_url = reverse_lazy('locations_list')
