
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
    template_name = "locations/partials/new_location_form.html"
    success_url = reverse_lazy("venue_list")

    def form_valid(self, form):
        venue = form.save()
        if self.request.htmx:  # if request came from HTMX
            return render(self.request, "venues/partials/venue_row.html", {"venue": venue})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.htmx:
            # Re-render the form with errors, but only the partial
            return render(self.request, "venues/partials/venue_form.html", {"form": form})
        return super().form_invalid(form)
