from django.contrib import admin

from .models import Division, Season, TeamContact, Team, TeamCollection, Field, Schedule
# Register your models here.

admin.site.register(Division)
admin.site.register(Season)
admin.site.register(TeamContact)
admin.site.register(Team)
admin.site.register(TeamCollection)
admin.site.register(Field)
admin.site.register(Schedule)
