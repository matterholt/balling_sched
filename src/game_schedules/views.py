import csv


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Venue
from .forms import VenueForm, UploadVenueForm

from django.http import HttpResponse
from curses.ascii import ENQ
from uu import decode
# Create your views here.
def index(request):
  return HttpResponse("Schedules for the upcoming season.")

def year(request,year):
    # Fetch and render the full schedule
    return HttpResponse(f"Full schedule for the upcoming season.asd for {year}")



# CRUD for locations

class VenueListView(ListView):
    model = Venue
    template_name = 'locations/locations_list.html'
    context_object_name = 'locations'


def upload_csv(request):
    if request.method == 'POST':
      form = UploadVenueForm(request.POST, request.FILES)
      if form.is_valid():
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
          messages.error(request, "Invalid file format. Please upload a CSV file.")
          return redirect("upload_csv")

        file_data = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(file_data)

        for row in reader:
            venue = Venue.objects.create(
                name=row['name'],
                address=row['address'],
                city=row['city'],
                state=row['state'],
                zip_code=row['zip_code'],
                phone=row['phone'],
                email=row['email'],
                website=row['website'],
                notes=row['notes']
            )
            messages.success(request, "CSV file imported successfully!")
            return redirect("upload_csv")
