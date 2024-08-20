from django.db import models
from match.models import Match
from player.models import Player

class ExtraType(models.Model):
    name = models.CharField(max_length=50)

class DismissalType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class ShotZone(models.Model):
    name = models.CharField(max_length=50)

class WagonWheel(models.Model):
    name = models.CharField(max_length=50)

class Length(models.Model):
    name = models.CharField(max_length=50)

class BowlingSide(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class DeliverySide(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class CreaseMovement(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class ShotConnection(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class BatSubject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Stroke(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class KeeperActivity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class BatsmanActivity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class FieldingActivity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class UmpireActivity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Ball(models.Model):
    ballNumber = models.IntegerField()
    over = models.IntegerField()
    matchId = models.ForeignKey(Match,on_delete=models.CASCADE)
    innings = models.IntegerField()
    striker = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='balls_striker')
    nonStriker = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='balls_non_striker')
    bowler = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='balls_bowler')
    runs = models.IntegerField()
    extra1 = models.IntegerField()
    extra2 = models.IntegerField()
    extraType1 = models.ForeignKey(ExtraType,on_delete=models.CASCADE,related_name='balls_extra_type1')
    extraType2 = models.ForeignKey(ExtraType,on_delete=models.CASCADE,related_name='balls_extra_type2')
    isDead = models.BooleanField()
    penalty = models.IntegerField()
    wide = models.IntegerField()
    noBall = models.IntegerField()
    isFreeHit = models.BooleanField()
    boundaryRuns = models.IntegerField()
    overThrow = models.IntegerField()
    ballSpeed = models.FloatField()
    ballSpeedMetric = models.CharField(max_length=50,choices=(('kph','kph'),('mph','mph')))
    swing = models.IntegerField()
    batSpeed = models.FloatField()
    isWicket = models.BooleanField()
    dismissalType = models.ForeignKey(DismissalType, on_delete=models.CASCADE)
    fielder1 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='balls_fielder1')
    fielder2 = models.ForeignKey(Player,on_delete=models.CASCADE,related_name='balls_fielder2')
    shortRuns = models.IntegerField()
    shotZone = models.ForeignKey(ShotZone,on_delete=models.CASCADE)
    wagonWheel = models.ForeignKey(WagonWheel,on_delete=models.CASCADE)
    length = models.ForeignKey(Length,on_delete=models.CASCADE)
    bowlingSide = models.ForeignKey(BowlingSide,on_delete=models.CASCADE)
    deliverySide = models.ForeignKey(DeliverySide,on_delete=models.CASCADE)
    creaseMovement = models.ForeignKey(CreaseMovement,on_delete=models.CASCADE)
    shotConnection = models.ForeignKey(ShotConnection,on_delete=models.CASCADE)
    batSubject = models.ForeignKey(BatSubject,on_delete=models.CASCADE)
    stroke = models.ForeignKey(Stroke,on_delete=models.CASCADE)
    keeperActivity = models.ForeignKey(KeeperActivity,on_delete=models.CASCADE)
    batsmanActivity = models.ForeignKey(BatsmanActivity,on_delete=models.CASCADE)
    fieldingActivity = models.ForeignKey(FieldingActivity,on_delete=models.CASCADE)
    umpireActivity = models.ForeignKey(UmpireActivity,on_delete=models.CASCADE)