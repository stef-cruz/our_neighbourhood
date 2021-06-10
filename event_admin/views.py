from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from contact.forms import Contact
from events.forms import Event


@login_required
def event_admin(request):
    """ A view to enable the superuser to access all contact requests
     and events """

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    contacts = Contact.objects.all()
    events = Event.objects.all()

    template = 'event_admin/event-admin.html'
    context = {
        'contacts': contacts,
        'events': events,
    }
    return render(request, template, context)


@login_required
def mark_as_resolved(request, contact_id):
    """ A view to enable the superuser to mark contact
    requests as resolved"""

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    try:
        contact = get_object_or_404(Contact, pk=contact_id)
        contact.is_resolved = True
        contact.save()
        messages.success(request, 'Contact request marked as resolved.')
        return redirect(reverse('event_admin'))
    except ValueError as e:
        messages.error(request, f"There was a problem to mark this contact request as resolved. Error: {e.code}.")


@login_required
def mark_as_paid(request, event_id):
    """ A view to enable the superuser to mark events as paid"""

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    try:
        event = get_object_or_404(Event, pk=event_id)
        event.is_paid = True
        event.save()
        messages.success(request, 'Event marked as paid.')
        return redirect(reverse('event_admin'))
    except ValueError as e:
        messages.error(request, f"There was a problem to mark this event as paid. Error: {e.code}.")
