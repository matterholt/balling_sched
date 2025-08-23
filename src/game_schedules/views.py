from django.shortcuts import render, get_object_or_404, redirect

from .models import Venue
from .forms import VenueForm

from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse("Schedules for the upcoming season.")

def year(request,year):
    # Fetch and render the full schedule
    return HttpResponse(f"Full schedule for the upcoming season.asd for {year}")



# CRUD for locations
def location(request):
    locations = Venue.objects.all()
    return render(request, 'locations/locations_list.html', {'locations': locations})
