from django.urls import path
from .views import *

urlpatterns = [
    path('all/',getAllTeamsByUserId,name='getAllTeams'),
    path('add/',addTeam,name='addTeam'),
    path('update/<int:team_id>/',updateTeam,name='updateTeam'),
    path('delete/<int:team_id>/',deleteTeam,name='deleteTeam'),
    path('search/',searchTeams,name='searchTeams'),
]