from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from profiles.models import UserProfile
from .models import Event
from .forms import EventForm


@login_required(login_url='login')
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
            messages.success(request, 'Event created successfully')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Event could not be created, please ensure the form is valid.')
    else:
        form = EventForm

    template = 'events/add-event.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
