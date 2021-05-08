from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages


@login_required(login_url='login')
def add_event(request):
    """ A view to enable the user to add events """
    template = 'events/add-event.html'

    return render(request, template)