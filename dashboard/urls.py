from django.urls import path
from .views import *

urlpatterns = [
    path('',displayHome,name='displayHome'),
    path('displayLogin/',displayLogin,name='displayLogin'),
    path('displayLogout/',displayLogout,name='displayLogout'),
    path('displaySignup/',displaySignup,name='displaySignup'),
    path('displayMyProducts/',displayMyProducts,name='displayMyProducts'),
    path('displayProductStore/',displayProductStore,name='displayProductStore')
]