from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import  DeleteView,CreateView

from ..models import Venue


# HTMX
class VenueDeleteHTMX(DeleteView):
  model = Venue
  success_url = reverse_lazy('locations_list')



class VenueCreateView(CreateView):
  model = Venue
  fields = ['name', 'address', 'city', 'state', 'zip_code']
  template_name = "locations/venue_create.html"
  success_url = reverse_lazy('locations_list')
