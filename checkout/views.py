from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.utils.datetime_safe import datetime
from django.contrib import messages


from .models import Order
from profiles.models import UserProfile
from events.forms import EventForm
from events.models import Event

import stripe


@login_required
def checkout(request):
    """ Checkout function to capture payment """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    event_session = request.session.get('event_session', {})

    if not event_session:
        return redirect(reverse('home'))

    if request.method == 'POST':
        # Change is_paid flag to true
        for key in event_session:
            event_paid = Event.objects.get(pk=key)
            event_paid.is_paid = True
            event_paid.save()

        # Create object in Order Table
        user = get_object_or_404(UserProfile, user=request.user)
        payment_date = datetime.now()

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

        form = EventForm()

    template = 'checkout/checkout.html'

    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request):
    """ Success checkout """
    event_session = request.session.get('event_session', {})

    if not event_session:
        return redirect(reverse('home'))

    user = get_object_or_404(UserProfile, user=request.user)

    template = 'checkout/checkout_success.html'

    context = {
        'user': user
    }

    return render(request, template, context)
