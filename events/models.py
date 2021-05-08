from django.db import models
from django.conf import settings


EVENTS_CATEGORY = (
    ('fitness', 'fitness'),
    ('services', 'services'),
    ('kids', 'kids'),
    ('business', 'business'),
    ('other', 'other'),
)


class Event(models.Model):
    """
    Events have to be linked to be user via a foreign key.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, editable=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=True)
    description = models.CharField(max_length=1000, blank=False, null=True)
    event_date = models.DateTimeField(blank=False, null=True)
    event_time = models.TimeField()
    event_price = models.CharField(max_length=50, blank=False, null=True)
    event_contact = models.CharField(max_length=100, blank=False, null=True)
    event_category = models.CharField(max_length=100, default='fitness', choices=EVENTS_CATEGORY)
    creation_date = models.DateTimeField(auto_now_add=True)
