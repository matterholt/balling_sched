import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.db import IntegrityError


# Create your views here.
def index(request):
    return HttpResponse("Schedules for the upcoming season.")


class ScheduledGames(ListView):
    template_name = "team_schedule/index.html"
    context_object_name = "games"
