from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ A view to return the profile page """

    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Something went wrong, '
                                    'please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    events = profile.events.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'events': events,
    }
    return render(request, template, context)


@login_required
def delete_profile(request, user):
    """ A view to delete current user"""

    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    try:
        if request.user.username == user:
            user = request.user
            user.delete()
            messages.success(request, 'Profile deleted successfully')
    except ValueError as e:
        messages.error(request, "There was a problem deleting your profile."
                                "Please contact us for assistance.")

    return redirect(reverse('home'))
