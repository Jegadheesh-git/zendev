from django.db import models
from django.contrib.auth.models import User

class Nationality(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.name

class HeightType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class BowlingType(models.Model):
    name = models.CharField(max_length=250)
    prefix = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class BattingType(models.Model):
    name = models.CharField(max_length=250)
    prefix = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class BowlerType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Player(models.Model):
    firstName = models.CharField(max_length=250,null=True,default=None, blank=True)
    middleName = models.CharField(max_length=250,null=True,default=None, blank=True)
    lastName = models.CharField(max_length=250,null=True,default=None, blank=True)
    nickName = models.CharField(max_length=250,null=True,default=None, blank=True)
    nationalityId = models.ForeignKey(Nationality,on_delete=models.CASCADE,null=True,default=None, blank=True)
    dob = models.DateField(null=True,default=None, blank=True)
    heightType = models.ForeignKey(HeightType,on_delete=models.CASCADE,null=True,default=None, blank=True)
    gender = models.IntegerField(null=True,default=None, blank=True)
    height = models.FloatField(null=True,default=None, blank=True)
    weight = models.FloatField(null=True,default=None, blank=True)
    batting = models.BooleanField(null=True,default=None, blank=True)
    bowling = models.BooleanField(null=True,default=None, blank=True)
    wicketKeeper = models.BooleanField(null=True,default=None, blank=True)
    fielding = models.BooleanField(null=True,default=None, blank=True)
    bowlingTypeId = models.ForeignKey(BowlingType,on_delete=models.CASCADE,null=True,default=None, blank=True)
    battingTypeId = models.ForeignKey(BattingType,on_delete=models.CASCADE,null=True,default=None, blank=True)
    
    bowlerTypeId = models.ForeignKey(BowlerType,on_delete=models.CASCADE,null=True,default=None, blank=True)
    pace = models.BooleanField(null=True,default=None, blank=True)
    spin = models.BooleanField(null=True,default=None, blank=True)
    ciPlayerId = models.IntegerField(null=True,default=None, blank=True) 

    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.firstName+' '+self.lastName

class Umpire(models.Model):
    name = models.CharField(max_length=250)
    nationality = models.ForeignKey(Nationality,on_delete=models.CASCADE)
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name 