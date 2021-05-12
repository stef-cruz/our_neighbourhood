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
                                 widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': '01/01/2021'}),
                                 input_formats=('%d/%m/%Y', ))

    # Time field - format HH:MM
    event_time = forms.TimeField(label='Time',
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

