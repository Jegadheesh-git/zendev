from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'


"""
Usage - This app used for user-accounts, supscription related data and payment functions

Models:

Sport        - sports name entries
Subscription - subscriptions for tools
UserSubscription - mapping user and subscription
Profile - Additional data about user

Views:

createPayment - creates a razorpay payment and add an user subscription entry
verifypayment - verfies the payment and make the subscription active
"""