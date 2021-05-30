from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from contact.forms import Contact
from events.forms import Event


@login_required
def event_admin(request):
    """ A view to enable the superuser to access all contact requests
     and events """

    contacts = Contact.objects.all()
    events = Event.objects.all()

    template = 'event_admin/event-admin.html'
    context = {
        'contacts': contacts,
        'events': events,
    }
    return render(request, template, context)

