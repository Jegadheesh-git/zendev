from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from accounts.models import *
from django.utils import timezone
# Create your views here.
def displayHome(request):
    return render(request,'index.html')

def displayLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Fetch all subscriptions for the logged-in user
            user_subscriptions = UserSubscription.objects.filter(user=user)

            # Check and update the isActive status
            for subscription in user_subscriptions:
                
                if subscription.endsOn and subscription.endsOn < timezone.now():
                    print(subscription.subscription.name+" expired!")
                    subscription.isActive = False
                    subscription.save()

            # Log in the user and redirect
            login(request, user)
            return redirect('displayMyProducts')
        else:
            return redirect('displayLogin') 
    return render(request, 'login.html')

def displayLogout(request):
    logout(request) 
    return redirect('displayHome')

def displaySignup(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        password = request.POST.get('password')
        company = request.POST.get('company')
        role = request.POST.get('role')
        hasAcceptedTC = True if request.POST.get('hasAcceptedTC')=='on' else False
        hasAcceptedPP = True if request.POST.get('hasAcceptedPP')=='on' else False
        hasAcceptedNL = True if request.POST.get('hasAcceptedNL')=='on' else False

        if User.objects.filter(email=email).exists():
            # Handle the case where the email is already in use
            return render(request, 'signup.html', {'error': 'An account with this email already exists'})
        
        user = User.objects.create_user(username=email,email=email,password=password)
        user.save()

        profile = Profile.objects.create(
            userAccount=user,
            firstName = firstName,
            lastName=lastName,
            company=company,
            role=role,
            hasAcceptedTC=hasAcceptedTC,
            hasAcceptedPP=hasAcceptedPP,
            hasAcceptedNL=hasAcceptedNL
            )
        redirect('displayMyProducts')
    return render(request,'signup.html')

def displayMyProducts(request):
    userSubscriptions = UserSubscription.objects.filter(user=request.user)
    print(userSubscriptions)
    return render(request,'myProducts.html',{'myProducts':userSubscriptions})

from django.db.models import Value, BooleanField

def displayProductStore(request):
    # Get all subscriptions
    products = Subscription.objects.all()

    # Get a set of subscription IDs that the user has already purchased
    userSubscriptions = set(UserSubscription.objects.filter(user=request.user).values_list('subscription_id', flat=True))

    # Annotate each product with a boolean indicating if it is already purchased
    products = products.annotate(
        isAlreadyPurchased=Value(False, output_field=BooleanField())
    )

    for product in products:
        if product.id in userSubscriptions:
            product.isAlreadyPurchased = True

    return render(request, 'productStore.html', {'products': products})
