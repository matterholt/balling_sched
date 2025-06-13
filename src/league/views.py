import csv
import io

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.utils.dateparse import parse_datetime


# Create your views here.
from .models import Season,TeamContact,TeamCollection,Team,Schedule,Division,Field
from .forms import EventForm,ScheduleCSVUploadForm

def index(request):
    seasons_for_play = Season.objects.all()
    all_people = TeamContact.objects.all()
    template = loader.get_template("explore.html")
    context = {"seasons_for_play": seasons_for_play,"all_people":all_people}
    return HttpResponse(template.render(context, request))


def user_dashboard(request, user_name):
    user_details = TeamContact.objects.get(name = user_name)

    associated_team = TeamCollection.objects.filter(contact = user_details.id)

    for i in associated_team:
        print(i.team)
        team_asigned = Team.objects.get(call_us = i.team)
        team_schedule = Schedule.objects.filter(team = i.team)
        print(team_asigned)
        print(team_schedule)




    template = loader.get_template("dashboard/index.html")
    context = {"user_details": user_details, "teams": associated_team}
    return HttpResponse(template.render(context, request))

def user_team(request,user_name,team_id):
    team_details = Team.objects.get(id = team_id)
    teams_admin  =  TeamCollection.objects.filter(team = team_id)
    team_schedule = Schedule.objects.filter(team = team_id)


    template = loader.get_template("dashboard/teams_page.html")
    context = {"team_details": team_details, "teams_admin": teams_admin, "team_schedule" : team_schedule , 'schedule_add_form':EventForm() ,'csv_schdule_form':ScheduleCSVUploadForm()}
    return HttpResponse(template.render(context, request))

def add_to_roster(request,addTo):
    pass

# @login_required # ADD LATER
@require_http_methods(['POST'])
def add_to_schedule(request,team_id):
    form = EventForm(request.POST)

    # TODO:  get data from team name
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

@require_http_methods(['POST'])
def upload_schedule_csv(request):
    form = ScheduleCSVUploadForm(request.POST, request.FILES)
    if form.is_valid():
        csv_file = form.cleaned_data['csv_file']
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)

        for row in reader:
            try:
                start_time = parse_datetime(row['start_time'].strip())
                end_time = parse_datetime(row['end_time'].strip())
                game_type = row['game_type'].strip()
                field = Field.objects.get(name=row['field_location'].strip())
                team = Team.objects.get(name=row['team'].strip())
                Schedule.objects.create(
                    start_time=start_time,
                    end_time=end_time,
                    game_type=game_type,
                    field_location=field,
                    team=team
                )

            except Exception as e:
                messages.error(request, f"Error processing row: {row}. Error: {e}")
                continue
        messages.success(request,f"CSV uploaded and schedules created")
        return redirect("schedul_list")

    else:
        form = ScheduleCSVUploadForm()

    return render(request, 'schedule/upload_csv.html', {'form': form})





@require_http_methods(['DELETE'])
def delete_event_schedule(request, event_id):
    Schedule.objects.filter(id=event_id).delete()

    teams_events = Schedule.objects.filter(team = team_id)
    context ={"team_schedule": teams_events}

    template = loader.get_template("dashboard/blocks/schedule_row.html")
    return HttpResponse(template.render(context, request))
