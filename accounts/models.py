from django.db import models
from django.contrib.auth.models import User

# sport related entries
class Sport(models.Model):
    name = models.CharField(max_length=50) # name of the sport

    def __str__(self) -> str:
        return self.name

# subscription for tools
class Subscription(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
    validityInDays = models.IntegerField()
    isActive = models.BooleanField(default=True)
    price = models.FloatField()
    addedOn = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=250,default='')



class UserSubscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE)
    startsFrom = models.DateTimeField(auto_now_add=True)
    endsOn = models.DateTimeField(null=True,blank=True)
    isActive = models.BooleanField(default=False)

class Profile(models.Model):
    userAccount = models.OneToOneField(User,null=True,blank=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    favSport = models.CharField(max_length=50)
    hasAcceptedTC = models.BooleanField(default=False)
    hasAcceptedPP = models.BooleanField(default=False)
    hasAcceptedNL = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.userAccount.username