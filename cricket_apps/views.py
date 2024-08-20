from django.shortcuts import render
from accounts.models import *
from django.http import JsonResponse

# Create your views here.
def displayAdvancedCricketDashboard(request):
    subscription = Subscription.objects.get(pk=1)
    
    userSubscription = UserSubscription.objects.filter(user=request.user, subscription=subscription,isActive=True)
    if len(userSubscription)==0:
        return JsonResponse({'error':'Cant access the product'},status=400)
    return render(request,'base.html')
    