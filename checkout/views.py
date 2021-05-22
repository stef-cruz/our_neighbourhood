from django.shortcuts import render
from django.conf import settings

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe_amount = round(1 * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_amount,
        currency = settings.STRIPE_CURRENCY
    )

    template = 'checkout/checkout.html'

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
