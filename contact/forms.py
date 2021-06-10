from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    # Name field
    contact_name = forms.CharField(label='Name',
                                   max_length=100,
                                   required=True,
                                   widget=forms.TextInput
                                   (attrs={'placeholder': 'Your name'}))

    # Email field
    contact_email = forms.EmailField(label='Email',
                                     max_length=100,
                                     required=True,
                                     error_messages={'invalid': 'Please '
                                                                'enter a valid email address.'},
                                     widget=forms.TextInput
                                     (attrs={'placeholder': 'Your email'}))

    # Message field
    message = forms.CharField(label='Message',
                              max_length=2000,
                              required=True,
                              widget=forms.Textarea
                              (attrs={'placeholder': 'Message'}))

    class Meta:
        model = Contact
        fields = ['contact_category',
                  'contact_name',
                  'contact_email',
                  'message']

        labels = {
            'contact_category': 'Reason for contact'
        }
