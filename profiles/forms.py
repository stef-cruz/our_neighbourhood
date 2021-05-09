from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    bio = forms.CharField(max_length=2000, required=True, widget=forms.Textarea)

    class Meta:
        model = UserProfile
        fields = ['full_name', 'email_address', 'bio', 'profile_pic']

        labels = {
            'full_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Name',
            'email_address': 'Email Address',
            'bio': 'Add a bio',
        }

        for field in self.fields:
            if field != 'profile_pic':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
