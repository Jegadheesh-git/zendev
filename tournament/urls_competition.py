from django.urls import path
from .views_competition import *

urlpatterns = [
    path('all/',getAllCompetitions,name='getAllCompetitions'),
    path('all/<int:tournamentId>/',getAllCompetitionsByTournament,name='getAllCompetitionsByTournament'),
    path('profile/<int:competition_id>/',getCompetitionById,name='getCompetitionById'),
    path('add/',addCompetition,name='addCompetition'),
    path('addCompetitionTeam/<int:competitionId>/',addCompetitionTeams,name='addCompetitionTeams'),
    path('addCompetitionSquad/<int:competitionId>/',addCompetitionSquad,name='addCompetitionSquad'),

    path('update/<int:competition_id>/',updateCompetition,name='updateCompetition'),
    path('updateCompetitionTeams/<int:competitionId>/',updateCompetitionTeams,name='updateCompetitionTeams'),
    path('updateCompetitionSquad/',updateCompetitionSquad,name='updateCompetitionSquad'),
    path('delete/<int:competition_id>/',deleteCompetition,name='deleteCompetition'),

    path('search/',searchCompetition,name='searchCompetition'),
]