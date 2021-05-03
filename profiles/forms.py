from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'email_address', 'bio', 'profile_pic']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user': 'Username',
            'full_name': 'Name',
            'email_address': 'Email Address',
            'bio': 'Add a bio',
        }
