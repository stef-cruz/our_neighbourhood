from django.shortcuts import render

from events.models import Event

def index(request):
    """ A view to return the index page """

    events = Event.objects.all()

    template = 'home/index.html'

    context = {
        'events': events,
    }

    return render(request, template, context)