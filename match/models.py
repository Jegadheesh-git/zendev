from django.db import models
from django.contrib.auth.models import User
from tournament.models import Competition,MatchType
from team.models import Team
from player.models import Player,Umpire, Nationality


# Create your models here.
class Stadium(models.Model):
    name = models.CharField(max_length=250)
    nationality = models.ForeignKey(Nationality,null=True,blank=True,on_delete=models.CASCADE)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)

class Knockout(models.Model):
    name = models.CharField(max_length=250)

class Match(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    date = models.DateField()
    matchType = models.ForeignKey(MatchType,on_delete=models.CASCADE)
    dayOrNight = models.CharField(max_length=15, choices=(('Day', 'Day'), ('Night', 'Night'), ('DayNight', 'DayNight')))
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_teamA')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_teamB')
    
    knockout = models.ForeignKey(Knockout,on_delete=models.CASCADE)

    # Toss details
    tossWonBy = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_toss_won_by', null=True,blank=True)
    optTo = models.CharField(max_length=15, choices=(('Batting', 'Batting'), ('Fielding', 'Fielding')), null=True,blank=True)
    fisrtInningsCondition = models.CharField(max_length=15, choices=(('Day', 'Day'), ('Under Lights', 'Under Lights')), null=True,blank=True)
    secondInningsCondition = models.CharField(max_length=25, choices=(('Day', 'Day'), ('Under Lights', 'Under Lights')), null=True,blank=True)

    teamBattingFirst = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='matches_teamBattingFirst', null=True,blank=True)
    teamBattingSecond = models.ForeignKey(Team,on_delete=models.CASCADE,related_name='matches_teamBattingSecond', null=True,blank=True)

    umpire1 = models.ForeignKey(Umpire,null=True,blank=True,on_delete=models.CASCADE,related_name='matches_umpire1')
    umpire2 = models.ForeignKey(Umpire,null=True,blank=True,on_delete=models.CASCADE,related_name='matches_umpire2')
    umpire3 = models.ForeignKey(Umpire,null=True,blank=True,on_delete=models.CASCADE,related_name='matches_umpire3')


    # Captain and Wicketkeeper

    captain1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_captainA', null=True,blank=True)
    wicketKeeper1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_wicket_keeperA', null=True,blank=True)
    captain2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_captainB', null=True,blank=True)
    wicketKeeper2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_wicket_keeperB', null=True,blank=True)

    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)

class PlayingEleven(models.Model):
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    innings = models.IntegerField(null=True,blank=True)
    battingOrder = models.IntegerField()
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    player = models.ForeignKey(Player,on_delete=models.CASCADE)
    substitute = models.BooleanField(default=False)
    dismissed = models.BooleanField(default=False)