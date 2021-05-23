from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.utils.datetime_safe import datetime

from .models import Order
from profiles.models import UserProfile

import stripe


@login_required
def checkout(request):
    """ Checkout function to capture payment """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        payment_date = datetime.now()
        user = get_object_or_404(UserProfile, user=request.user)

        Order.objects.create(
            user=user, amount='1.00',
            payment_date=payment_date)

        return redirect(reverse('checkout_success'))

    else:
        stripe_amount = round(1 * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_amount,
            currency=settings.STRIPE_CURRENCY
        )

    template = 'checkout/checkout.html'

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request):
    """ Success checkout """
    user = get_object_or_404(UserProfile, user=request.user)

    print(user)

    template = 'checkout/checkout_success.html'

    context = {
        'user': user
    }

    return render(request, template, context)
