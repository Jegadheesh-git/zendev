from django.urls import path
from .views import *

urlpatterns = [
    path('',getPlayerDashboard,name='getPlayerDashboard'),
    path('all/',getAllPlayersByUserId,name='getAllPlayersByUserId'),
    path('profile/<int:player_id>/',getPlayerById,name='getPlayerById'),
    path('add/',addPlayer,name='addPlayer'),
    path('update/<int:player_id>/',updatePlayer,name='updatePlayer'),
    path('delete/<int:player_id>/',deletePlayer,name='deletePlayer'),

    path('search/',searchPlayers,name='searchPlayers'),

    path('umpire/all/',getAllUmpiresByUserId,name='getAllUmpiresByUserId'),
    path('umpire/add/',addUmpire,name='addUmpire'),
    path('umpire/delete/<int:umpire_id>/',deleteUmpire,name='deleteUmpire'),

]