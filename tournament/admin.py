from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Tournament)
admin.site.register(MatchType)
admin.site.register(Competition)
admin.site.register(CompetitionSquad)

