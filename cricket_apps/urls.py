from django.urls import path
from .views import *

urlpatterns = [
    path('displayAdvancedCricketDashboard/',displayAdvancedCricketDashboard,name='displayAdvancedCricketDashboard'),
]