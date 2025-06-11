from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:user_name>/dashboard/", views.user_dashboard, name="user_dashboard"),
    path("<str:user_name>/team/<int:team_id>", views.user_team, name="team_details"),
    path("<str:user_name>/team/<int:team_id>/roster", views.add_to_roster, name="team_roster"),
    path('schedule/teams/<int:team_id>/schedule/add/', views.add_to_schedule, name="add_to_schedule"),
    path('schedule/teams/<int:event_id>/schedule/delete/', views.delete_event_schedule, name="delete_event_schedule")
]
