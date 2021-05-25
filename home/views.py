from django.shortcuts import render
from django.core.paginator import Paginator

from events.models import Event


def index(request):
    """ A view to return the index page which displays
        the events created by the users """

    # Source fix to issue unordered object list warning https://stackoverflow.com/questions/44033670/python-django-rest-framework-unorderedobjectlistwarning
    events = Event.objects.filter(is_paid=True).order_by('id')

    paginator = Paginator(events, 8)  # Shows 8 events per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = 'home/index.html'

    context = {
        'events': events,
        'page_obj': page_obj,
    }

    return render(request, template, context)
