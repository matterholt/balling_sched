from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
  return HttpResponse("Schedules for the upcoming season.")

def year(request,year):
    # Fetch and render the full schedule
    return HttpResponse(f"Full schedule for the upcoming season. for {year}")
