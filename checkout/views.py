from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.utils.datetime_safe import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

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

    event_session = request.session.get('event_session')

    if not event_session:
        return redirect(reverse('home'))

    if request.method == 'POST':
        try:
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

        except stripe.error.CardError as e:
            messages.info(request, f"There was a problem processing your payment. Error: {e.code}.")

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

    # get user email address
    user_from_allauth = get_object_or_404(User, username=request.user)
    user_from_allauth_email_address = user_from_allauth.email

    # get username
    user = get_object_or_404(UserProfile, user=request.user)

    subject, from_email, to = 'Our Neighbourhood Order Confirmation', \
                              settings.EMAIL_HOST_USER, user_from_allauth_email_address
    text_content = f'Hi {user}, Thank you for posting an event on Our Neighbourhood.'
    html_content = '<h3 style="color:#5710b2;">Our Neighbourhood - Order received</h3>' \
                   f'<p>Hi <strong>{user}</strong>, </p>' \
                   f'<p> Thank you for posting an event on Our Neighbourhood.</p>' \
                   '<p>If you need assistance, please contact us ' \
                   '<a href="https://ci-milestone4.herokuapp.com/contact/" target="_blank">here</a>.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    if request.session:
        try:
            del request.session['event_session']
        except:
            return redirect(reverse('home'))

    template = 'checkout/checkout_success.html'

    context = {
        'user_from_allauth_email_address': user_from_allauth_email_address,
    }

    return render(request, template, context)
