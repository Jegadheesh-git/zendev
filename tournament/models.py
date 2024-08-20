from django.db import models
from player.models import Player, Umpire
from team.models import Team
from django.contrib.auth.models import User

class Tournament(models.Model):
    name = models.CharField(max_length=250)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)

class MatchType(models.Model):
    name = models.CharField(max_length=250)
    innings = models.IntegerField(default=2)
    isLimitedOvers = models.BooleanField(default=True)
    activePlayersPerTeam = models.IntegerField(default=11)
    oversPerInnings = models.IntegerField()
    ballsPerOver = models.IntegerField()
    widePenaltyRuns = models.IntegerField()
    noBallPenaltyRuns = models.IntegerField()
    hasFreeHit = models.BooleanField()
    hasTie = models.BooleanField()
    hasNoResult = models.BooleanField()


class Competition(models.Model):
    name = models.CharField(max_length=250)
    displayName = models.CharField(max_length=250)
    year = models.IntegerField()
    matchType = models.ForeignKey(MatchType,on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    fromDate = models.DateField()
    toDate = models.DateField()
    matchCount = models.IntegerField()
    gender = models.CharField(max_length=15,choices=(('Male','Male'),('Female','Female'),('Third gender','Third gender')))
    teams = models.ManyToManyField(Team)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)

class CompetitionSquad(models.Model):
    competition = models.ForeignKey(Competition,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    players = models.ManyToManyField(Player)