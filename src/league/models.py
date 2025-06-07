from datetime import datetime
from django.db import models

class Season(models.Model):
    description = models.CharField(max_length=200,default=f"Season {datetime.now().year}")
    start_date = models.DateField("start of season")
    end_date = models.DateField("end of season")

    def __str__ (self):
        return f'{self.description}'

# Create your models here.
class Division(models.Model):
    title = models.CharField(max_length=200)
    league = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__ (self):
        return f'{self.title} of {self.league}'

class TeamContact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    player_count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}'

class Team(models.Model):
    call_us = models.CharField(max_length=200)
    league_name = models.CharField(max_length=200,default="league name")
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.call_us} in {self.division}'

class TeamCollection(models.Model):
    TEAM_OPTIONS=[
        ("coach","coach"),
        ("ast. coach","ast. coach"),
        ("player","player")
    ]
    contact = models.ForeignKey(TeamContact, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_role = models.CharField(max_length=15, choices=TEAM_OPTIONS)

    def __str__(self):
        return f'{self.contact} is {self.team_role} for {self.team}'

class Field(models.Model):
    location = models.CharField(max_length=200)
    field_name = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.field_name} at {self.location}'

class Schedule(models.Model):
    GAME_OPTIONS=[
        ("practice","practice"),
        ("scrimmage","scrimmage"),
        ("game","game"),
        ("playoff","playoff")
    ]

    start_time  = models.DateTimeField("start of event")
    end_time  = models.DateTimeField("end of event")
    game_type= models.CharField(max_length=15, choices=GAME_OPTIONS)
    field_location = models.ForeignKey(Field, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # opponents  = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game_type} for {self.team}'

    # def duration(self) -> str:

    #     fmt = "%H:%M"
    #     start = datetime.strptime(self.start_time, fmt)
    #     end = datetime.strptime(self.end_time, fmt)
    #     duration = end - start
    #     total_minutes = duration.total_seconds() // 60
    #     hours = int(total_minutes // 60)
    #     minutes = int(total_minutes % 60)
    #     return f"{hours} hours, {minutes} minutes"

# Example usage
