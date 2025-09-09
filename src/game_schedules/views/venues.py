
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import Venue
from ..forms import VenueForm

class VenueListView(ListView):
  model = Venue
  template_name = "locations/locations.html"
  context_object_name = "locations"



class VenueCreatePage(CreateView):
    model = Venue
    form_class = VenueForm
    template_name = "locations/subpages/add_location.html"
    success_url = reverse_lazy("locations_list")

class VenueEditPage(UpdateView):
    model = Venue
    form_class = VenueForm
    template_name = "locations/subpages/edit_location.html"
    success_url = reverse_lazy("locations_list")
