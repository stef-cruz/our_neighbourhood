from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    # Name field
    full_name = forms.CharField(label='Name',
                                max_length=50,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Name'}))

    # Description field
    bio = forms.CharField(label='Bio',
                          max_length=1500,
                          required=False,
                          widget=forms.Textarea(attrs={'placeholder': 'Add a bio'}))

    class Meta:
        model = UserProfile
        fields = ['full_name', 'email_address', 'bio', 'profile_pic']

    def clean_title(self):
        full_name = self.cleaned_data.get('title')
        if full_name.isalnum() or " " in full_name:
            return full_name
        raise forms.ValidationError('Only letters and numbers allowed.')
