from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe
import json


@require_POST
@csrf_exempt
def webhook(request):
    """ Listen for Stripe webhooks """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    # Get webhook data
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(content=e, status=400)

    print('Success')
    return HttpResponse(status=200)


