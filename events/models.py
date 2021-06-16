from django.db import models
from django.core.validators import RegexValidator

from profiles.models import UserProfile

EVENTS_CATEGORY = (
    ('Arts', 'Arts'),
    ('Food & Drinks', 'Food & Drinks'),
    ('Fitness & Sports', 'Fitness & Sports'),
    ('Kids', 'Kids'),
    ('Services', 'Services'),
    ('Other', 'Other'),
)

no_alpha = RegexValidator(r'^[ ]*[A-Za-z0-9][A-Za-z0-9 ]*$',
                          'Only letters and numbers allowed.')


class Event(models.Model):
    """
    Events have to be linked to be user via a foreign key.
    """
    user = models.ForeignKey(UserProfile,
                             on_delete=models.CASCADE,
                             null=True, related_name='events')
    title = models.CharField(max_length=100, blank=False,
                             null=True, validators=[no_alpha])
    description = models.CharField(max_length=1000,
                                   blank=False, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(max_length=50, blank=True, null=True)
    event_location = models.CharField(max_length=150, blank=True,
                                      null=True, validators=[no_alpha])
    event_price = models.CharField(max_length=50, blank=False,
                                   null=True, validators=[no_alpha])
    event_contact = models.CharField(max_length=100, blank=False,
                                     null=True)
    event_category = models.CharField(max_length=100,
                                      default='Arts', choices=EVENTS_CATEGORY)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False, blank=True, null=True)
