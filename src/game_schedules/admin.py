from django.contrib import admin

from .models import TeamDivision, Venue, SeasonSchedule

admin.site.register(TeamDivision)
admin.site.register(Venue)
admin.site.register(SeasonSchedule)
