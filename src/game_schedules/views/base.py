import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.db import IntegrityError

from ..models import Venue
from ..forms import  UploadVenueForm



# Create your views here.
def index(request):
    return HttpResponse("Schedules for the upcoming season.")

class ScheduledGames(ListView):
    model = Venue

    template_name = "team_schedule/index.html"
    context_object_name = "games"




# covert to classes
def spreadsheet_upload(request):
    duplicated_entries = []

    if request.method == "POST":
        form = UploadVenueForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES["file"]

            if not csv_file.name.endswith(".csv"):
                messages.error(
                    request, "Invalid file format. Please upload a CSV file."
                )
                return redirect("locations_list")

            file_data = csv_file.read().decode("utf-8").splitlines()
            reader = csv.DictReader(file_data)

            for row in reader:
                try:
                    Venue.objects.create(
                        short_name=row["short_name"],
                        name=row["name"],
                        address=row["address"],
                        city=row["city"],
                        state=row["state"],
                        zip_code=row["zip_code"],
                    )
                except IntegrityError:
                    duplicated_entries.append(row["short_name"])

                    continue

        if duplicated_entries:
            messages.warning(
                request, f"Skipped duplicates: {', '.join(duplicated_entries)}"
            )
        else:
            messages.success(request, "CSV file imported successfully!")
        # return redirect("locations_list")
    else:
        form = UploadVenueForm()

    return render(request, "locations/spreadsheet_upload.html", {"form": form})
