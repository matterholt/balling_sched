from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


# Create your views here.
from .models import Season,TeamContact,TeamCollection,Team,Schedule
def index(request):
    seasons_for_play = Season.objects.all()
    all_people = TeamContact.objects.all()
    template = loader.get_template("explore.html")
    context = {"seasons_for_play": seasons_for_play,"all_people":all_people}
    return HttpResponse(template.render(context, request))


def user_dashboard(request, user_name):
    user_details = TeamContact.objects.get(name = user_name)
    associated_team = TeamCollection.objects.filter(contact = user_details.id)
    template = loader.get_template("dashboard/index.html")
    context = {"user_details": user_details, "teams": associated_team}
    return HttpResponse(template.render(context, request))

def user_team(request,user_name,team_id):
    team_details = Team.objects.get(id = team_id)
    teams_admin  =  TeamCollection.objects.filter(team = team_id)
    team_schedule = Schedule.objects.filter(team = team_id)

    template = loader.get_template("dashboard/teams_page.html")
    context = {"team_details": team_details, "teams_admin": teams_admin, "team_schedule" : team_schedule }
    return HttpResponse(template.render(context, request))

def add_to_roster(request,addTo):
    pass
