from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


# Create your views here.
from .models import Season,TeamContact,TeamCollection,Team,Schedule,Division
from .forms import EventForm

def index(request):
    seasons_for_play = Season.objects.all()
    all_people = TeamContact.objects.all()
    template = loader.get_template("explore.html")
    context = {"seasons_for_play": seasons_for_play,"all_people":all_people}
    return HttpResponse(template.render(context, request))


def user_dashboard(request, user_name):
    user_details = TeamContact.objects.get(name = user_name)
    tasks = Division.objects.all()
    associated_team = TeamCollection.objects.filter(contact = user_details.id)
    template = loader.get_template("dashboard/index.html")
    context = {"user_details": user_details, "teams": associated_team, "tasks":tasks}
    return HttpResponse(template.render(context, request))

def user_team(request,user_name,team_id):
    team_details = Team.objects.get(id = team_id)
    teams_admin  =  TeamCollection.objects.filter(team = team_id)
    team_schedule = Schedule.objects.filter(team = team_id)


    template = loader.get_template("dashboard/teams_page.html")
    context = {"team_details": team_details, "teams_admin": teams_admin, "team_schedule" : team_schedule , 'schedule_add_form':EventForm() }
    return HttpResponse(template.render(context, request))

def add_to_roster(request,addTo):
    pass

# @login_required # ADD LATER
@require_http_methods(['POST'])
def add_to_schedule(request):
    form = EventForm(request.POST)
    if form.is_valid():
        form.save()
        template = loader.get_template("dashboard/blocks/schedule_row.html")
        teams_admin  =  Schedule.objects.all()
        context ={"team_schedule": teams_admin}

        # Return updated fragment
        return HttpResponse(template.render(context, request))
    else:
          form = EventForm()

    return HttpResponse("<p>DID not work.</p>")


@require_http_methods(['DELETE'])
def delete_task(request, id):
    Division.objects.filter(id=id).delete()
    tasks = Division.objects.all()
    return render(request, 'dashboard/tasks_list.html', {'tasks': tasks})
