from django.urls import path
from .views import ScheduledGames

urlpatterns = [
    path("", ScheduledGames.as_view(), name="index"),
]
