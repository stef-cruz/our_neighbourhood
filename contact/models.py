from django.db import models
from django.core.validators import RegexValidator

CONTACT_CATEGORY = (
    ('general_query', 'General Query'),
    ('event_issue', 'Event issue'),
    ('profile_issue', 'Profile issue'),
    ('payment_issue', 'Payment issue'),
)

no_alpha = RegexValidator(r'^[a-zA-Z0-9]+$',
                          'Only letters and numbers allowed.')


class Contact(models.Model):
    """
    A Contact model for the users to get in touch with the site
    """
    contact_category = models.CharField(max_length=100,
                                        choices=CONTACT_CATEGORY,
                                        default='general_query',
                                        null=False, blank=False)
    contact_name = models.CharField(max_length=80, null=False,
                                    blank=False, validators=[no_alpha])
    contact_email = models.EmailField(max_length=80,
                                      null=True, blank=True)
    message = models.CharField(max_length=1500,
                               null=False, blank=False)
    is_resolved = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact_name
