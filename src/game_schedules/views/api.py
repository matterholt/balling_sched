from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import  DeleteView

from ..models import Venue


# HTMX
class VenueDeleteHTMX(DeleteView):
  model = Venue
  success_url = reverse_lazy('locations_list')

  def delete(self, request, *args, **kwargs) -> HttpResponse | HttpResponseRedirect:

    self.object = self.get_object()
    self.object.delete()

    if request.headers.get('HX-Request'):
      return HttpResponse(status=204)

    # return super().delete(request, *args, **kwargs)
    return HttpResponseRedirect(self.success_url)
