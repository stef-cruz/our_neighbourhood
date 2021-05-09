from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    description = forms.CharField(max_length=2000, required=True, widget=forms.Textarea)

    class Meta:
        model = Event
        fields = ['title',
                  'description',
                  'event_date',
                  'event_time',
                  'event_price',
                  'event_contact',
                  'event_category']

        labels = {
            'title': 'Title',
            'description': 'Description',
            'event_date': 'Date',
            'event_time': 'Time',
            'event_price': 'Price',
            'event_contact': 'Contact',
            'event_category': 'Category'
        }

        def __init__(self, *args, **kwargs):
            """
            Add placeholders
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'title': 'Event title',
                'description': 'What is the event about?',
                'event_contact': 'Add a contact name and number',
            }

            for field in self.fields:
                if field != 'event_category':
                    if self.fields[field].required:
                        placeholder = f'{placeholders[field]} *'
                    else:
                        placeholder = placeholders[field]
                    self.fields[field].widget.attrs['placeholder'] = placeholder
