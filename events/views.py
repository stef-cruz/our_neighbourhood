from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.utils.datetime_safe import datetime

from profiles.models import UserProfile
from .models import Event
from .forms import EventForm


def event_detail(request, event_id):
    """ A view to show individual event details """

    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/event-detail.html', context)


def all_events(request):
    """ Display all events including sorting and search queries """

    # Source fix to issue unordered object list warning
    # https://stackoverflow.com/questions/44033670/python-django-rest-framework-unorderedobjectlistwarning
    events = Event.objects.filter(is_paid=True).order_by('id')
    query = None
    category = None
    date = None

    if request.GET:
        if 'date' in request.GET:
            date_event = request.GET['date']
            print(date_event)
            if date_event == 'upcoming-events':
                events = events.filter(event_date__gt=datetime.now())

        if 'category' in request.GET:
            categories = request.GET['category']
            if categories == 'arts':
                events = events.filter(event_category__icontains='arts')
            elif categories == 'food-and-drinks':
                events = events.filter(event_category__icontains='food')
            elif categories == 'fitness-and-sports':
                events = events.filter(event_category__icontains='fitness')
            elif categories == 'kids':
                events = events.filter(event_category__icontains='kids')
            elif categories == 'services':
                events = events.filter(event_category__icontains='services')
            else:
                events = events.filter(event_category__icontains='other')

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('events'))

            # Q is the only way to filter with an OR operator and
            # i in icontains makes it case insensitive
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            events = events.filter(queries)

    paginator = Paginator(events, 8)  # Shows 8 events per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = 'events/events.html'

    context = {
        'events': events,
        'page_obj': page_obj,
    }

    return render(request, template, context)


@login_required
def add_event(request):
    """ A view to enable the user to add events """

    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == 'POST':
        # instantiate the form
        form = EventForm(request.POST)
        # get user
        user = get_object_or_404(UserProfile, user=request.user)

        if form.is_valid():
            # store form instance in a variable
            event = form.save(commit=False)
            # assign user
            event.user = user
            # save to DB
            event.save()
            return redirect(reverse('preview_event', args=[event.id]))
        else:
            messages.error(request, 'Event could not be created, please ensure the form is valid.')
    else:
        form = EventForm

    template = 'events/add-event.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def preview_event(request, event_id):
    """ Preview event before payment """

    # if event has been already paid in the DB, redirect to home and
    # prevent session to be stored in the browser
    event_is_paid = Event.objects.get(pk=event_id)
    if event_is_paid.is_paid:
        return redirect(reverse('home'))

    # check if session exists, if not create session dict
    event_session = request.session.get('event_session', {})
    # get event id
    event = get_object_or_404(Event, pk=event_id)
    # update session's title
    event_session[event_id] = event.title
    # update session
    request.session['event_session'] = event_session

    context = {
        'event': event,
    }

    return render(request, 'events/preview-event.html', context)


@login_required
def edit_event(request, event_id):
    """ A view to enable the user to edit events """

    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    user_db = get_object_or_404(UserProfile, user=request.user)

    # check if event is created by the user editing it
    if event.user == user_db or request.user.is_superuser:
        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                messages.success(request, 'Event updated successfully.')
                if request.user.is_superuser:
                    return redirect(reverse('event_admin'))
                return redirect(reverse('event_detail', args=[event.id]))
            else:
                messages.error(request, 'Event could not be updated, please ensure the form is valid.')
        else:
            form = EventForm(instance=event)
            messages.info(request, f'You are editing {event.title}')

    # if event is not created by the user editing it
    else:
        messages.error(request, 'You do not have permission to edit this event.')
        return redirect(reverse('home'))

    template = 'events/edit-event.html'
    context = {
        'form': form,
        'event': event,
        'user_db': user_db,
    }
    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """ A view to enable the user to delete events """

    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    user_db = get_object_or_404(UserProfile, user=request.user)

    if event.user == user_db or request.user.is_superuser:
        event.delete()
        messages.success(request, 'Event successfully deleted.')
        if request.user.is_superuser:
            return redirect(reverse('event_admin'))
        return redirect(reverse('profile'))

    else:
        messages.error(request, 'You do not have permission to delete this event.')
        return redirect(reverse('profile'))
