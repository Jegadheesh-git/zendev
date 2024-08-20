from django.urls import path
from .views_stadium import *

urlpatterns = [
    path('all/',getAllStadiumsByUserId,name="getAllStadiumsByUserId"),
    path('add/',addStadium,name="addStadium"),
    path('delete/<int:stadium_id>/',deleteStadium,name="deleteStadium"),
]