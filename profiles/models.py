from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

no_alpha = RegexValidator(r'^[ ]*[A-Za-z0-9][A-Za-z0-9 ]*$', 'Only letters and numbers allowed.')


class UserProfile(models.Model):
    """
    A user profile model for maintaining the user's
    details and events
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False, validators=[no_alpha])
    email_address = models.EmailField(max_length=60, null=False, blank=True)
    bio = models.CharField(max_length=1500, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='upload/')
    creation_date = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
