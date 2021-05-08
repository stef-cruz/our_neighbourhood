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

        def __init__(self, *args, **kwargs):
            """
            Add placeholders
            """
            super().__init__(*args, **kwargs)
            placeholders = {
                'title': 'Event title',
                'description': 'Add as much information as possible',
                'event_contact': 'Add name, phone number, email address if relevant',
            }

            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
