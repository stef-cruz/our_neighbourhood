from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore

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
    if event.user == user_db:
        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                messages.success(request, 'Event updated successfully.')
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

    if event.user == user_db:
        event.delete()
        messages.success(request, 'Event successfully deleted.')
        return redirect(reverse('profile'))

    else:
        messages.error(request, 'You do not have permission to delete this event.')
        return redirect(reverse('profile'))
