import razorpay
from django.conf import settings
from django.http import JsonResponse
from .models import Subscription, UserSubscription 
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse


client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def createOrder(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Subscription.objects.get(id=product_id)

        #checking if the product is already subscribed
        userSubscription = UserSubscription.objects.filter(user=request.user,subscription=product)

        if(len(userSubscription)>0):
            return JsonResponse({'error': 'Product already Subscribed'}, status=400)
        amount = product.price * 100  # Razorpay amount is in paise
        currency = 'INR'
        
        # Create a Razorpay order
        order = client.order.create({
            'amount': amount,
            'currency': currency,
            'payment_capture': '1'
        })

        endsOn = timezone.now() + timedelta(days=product.validityInDays)

        userSubscription = UserSubscription(
            user = request.user,
            subscription = product,
            endsOn = endsOn
        )
        userSubscription.save()

        response_data = {
            'order_id': order['id'],
            'amount': amount,
            'currency': currency,
            'key_id': settings.RAZORPAY_KEY_ID,
            'subscription_id': userSubscription.pk,
        }
        print(response_data)
        return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def verifyPayment(request):
    if request.method == 'POST':
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')
        subscriptionId = request.POST.get('subscription_id')
        print(subscriptionId)
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

        try:
            # Verify the payment signature
            client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })

            # Payment is successful, you can now update the order status in your database
            # Order.objects.filter(order_id=order_id).update(status='Paid')
            userSubscription = UserSubscription.objects.get(pk=subscriptionId)
            userSubscription.isActive = True
            userSubscription.save()

            return JsonResponse({'status': 'success', 'redirect_url': reverse('displayMyProducts')})
        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({'status': 'error', 'message': 'Payment verification failed'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})