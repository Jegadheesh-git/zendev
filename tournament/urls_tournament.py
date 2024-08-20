from django.urls import path
from .views_tournament import *

urlpatterns = [
    path('all/',getAllTournamentsByUserId, name='getAllTournamentsByUserId'),
    path('add/',addTournament,name='addTournament'),
    path('update/<int:tournament_id>/',updateTournament,name='updateTournament'),
    path('delete/<int:tournament_id>/',deleteTournament,name='deleteTournament'),

    path('search/',searchTournaments,name='searchTournaments'),
]