from django.db import models
from player.models import Player
from django.contrib.auth.models import User

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=250)
    shortName = models.CharField(max_length=10)

    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name