
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from calendar import c
from ..models import Venue


class VenueListView(ListView):
  model = Venue
  template_name = "locations/locations_list.html"
  context_object_name = "locations"
