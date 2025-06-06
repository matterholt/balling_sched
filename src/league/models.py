from dill.tests.test_classdef import m
from django.db import models



# Create your models here.
class Division(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class TeamContact(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Team(models.Model):
    call_us = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

class TeamCollection(models.Model):
    TEAM_OPTIONS=[
        ("coach","coach"),
        ("ast. coach","ast. coach"),
        ("player","player")
    ]
    contact = models.ForeignKey(TeamContact, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team_role = models.CharField(max_length=15, choices=TEAM_OPTIONS)

class Field(models.Model):
    location = models.CharField(max_length=200)
    field_name = models.CharField(max_length=200)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

class Schedule(models.Model):
    field_location = models.ForeignKey(Field, on_delete=models.CASCADE)
    start_time  = models.CharField(max_length=200)
    end_time  = models.CharField(max_length=200)
    date  = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
