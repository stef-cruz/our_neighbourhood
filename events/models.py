from django.db import models
from django.conf import settings

from profiles.models import UserProfile

EVENTS_CATEGORY = (
    ('Arts', 'Arts'),
    ('Food & Drinks', 'Food & Drinks'),
    ('Fitness & Sports', 'Fitness & Sports'),
    ('Kids', 'Kids'),
    ('Services', 'Services'),
    ('Other', 'Other'),
)


class Event(models.Model):
    """
    Events have to be linked to be user via a foreign key.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, blank=True, related_name='events')
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=1000, blank=False, null=True)
    event_date = models.DateField(blank=False, null=True)
    event_time = models.TimeField(max_length=50, blank=False, null=True)
    event_price = models.CharField(max_length=50, blank=False, null=True)
    event_contact = models.CharField(max_length=100, blank=False, null=True)
    event_category = models.CharField(max_length=100, default='Arts', choices=EVENTS_CATEGORY)
    creation_date = models.DateTimeField(auto_now_add=True)
