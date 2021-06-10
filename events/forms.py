from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    # Title field
    title = forms.CharField(label='Title',
                            max_length=100,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Add the event title'}))

    # Description field
    description = forms.CharField(label='Description',
                                  max_length=2000,
                                  required=True,
                                  widget=forms.Textarea(attrs={'placeholder': 'Add the event description'}))

    # Date field - format DD/MM/YYYY
    event_date = forms.DateField(label='Date',
                                 required=False,
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': '01/01/2021'}),
                                 input_formats=('%d/%m/%Y', ))

    # Time field - format HH:MM
    event_time = forms.TimeField(label='Time',
                                 required=False,
                                 widget=forms.DateInput(format='%H:%M', attrs={'placeholder': '17:30'}),
                                 input_formats=('%H:%M', ))

    # Price field
    event_price = forms.CharField(label='Price',
                                  max_length=50,
                                  required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'e.g. 10 per person or Free'}))

    # Contact field
    event_contact = forms.CharField(label='Contact',
                                    max_length=100,
                                    required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'e.g. John Doe, 083 833 5566'}))

    # Location field
    event_location = forms.CharField(label='Location',
                                     max_length=150,
                                     required=False,
                                     widget=forms.TextInput(attrs={'placeholder': 'e.g. War Memorial Gardens'}))

    class Meta:
        model = Event
        fields = ['title',
                  'description',
                  'event_date',
                  'event_time',
                  'event_location',
                  'event_price',
                  'event_contact',
                  'event_category']

        labels = {
            'event_category': 'Category'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.isalnum() or " " in title:
            return title
        raise forms.ValidationError('Only letters and numbers allowed.')

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description.isalnum() or " " in description:
            return description
        raise forms.ValidationError('Only letters and numbers allowed.')

    def clean_event_price(self):
        event_price = self.cleaned_data.get('event_price')
        if event_price.isalnum() or " " in event_price:
            return event_price
        raise forms.ValidationError('Only letters and numbers allowed.')

    def clean_event_contact(self):
        event_contact = self.cleaned_data.get('event_contact')
        if event_contact.isalnum() or " " in event_contact:
            return event_contact
        raise forms.ValidationError('Only letters and numbers allowed.')

    def clean_event_location(self):
        event_location = self.cleaned_data.get('event_location')
        if event_location != "":
            if event_location.isalnum() or " " in event_location:
                return event_location
            raise forms.ValidationError('Only letters and numbers allowed.')
