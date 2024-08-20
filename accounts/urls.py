from django.urls import path
from .views import *

urlpatterns = [
    path('createOrder/',createOrder,name='createOrder'),
    path('verifyPayment/',verifyPayment,name='verifyPayment'),
]