from django.urls import path
from .views_match import *

urlpatterns =  [
    path('all/<int:competition_id>/',getAllMatchesByCompetition,name='getAllMatchesByCompetition'),
    path('add/<int:competition_id>/',addMatch,name='addMatch'),
    path('update/<int:match_id>/',updateMatchToss,name='updateMatchToss'),
    path('addxi/<int:match_id>/',addPlayingXI,name='addPlayingXI'),
    path('delete/<int:match_id>/',deleteMatch,name='deleteMatch'),
]