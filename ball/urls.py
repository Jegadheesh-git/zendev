from django.urls import path
from .views import *

urlpatterns = [
    path('add/<int:match_id>/',addBall,name='addBall'),
]