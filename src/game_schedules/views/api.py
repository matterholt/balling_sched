from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import  DeleteView,CreateView

from ..models import Venue


# HTMX
class VenueDeleteHTMX(DeleteView):
  model = Venue
  success_url = reverse_lazy('locations/partials/location_listing.html')

  def delete(self, request, *args, **kwargs) -> HttpResponse | HttpResponseRedirect:
      self.object = self.get_object()
      self.object.delete()

      if request.headers.get("HX-Request"):
          # HTMX request → just return 204 so htmx removes the element
          return HttpResponse(status=204)

      # Normal request → redirect to list
      return HttpResponseRedirect(self.success_url)


class VenueCreateView(CreateView):
  model = Venue
  fields = ['name', 'address', 'city', 'state', 'zip_code']
  template_name = "locations/venue_create.html"
  success_url = reverse_lazy('locations_list')
