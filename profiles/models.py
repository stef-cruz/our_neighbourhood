from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    A user profile model for maintaining the user's
    details and events
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.CharField(max_length=40, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    creation_date = models.CharField(max_length=80, null=True, blank=True)
    is_superuser = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username
