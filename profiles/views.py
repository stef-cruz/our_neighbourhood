from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ A view to return the profile page """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    # TODO: events = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        # 'events': events,
    }
    return render(request, template, context)


def delete_profile(request, user):
    """ A view to delete current user"""

    if not request.user.is_authenticated:
        return render(request, 'home/index.html')

    if request.user.username == user:
        user = request.user
        user.delete()

    return redirect(reverse('home'))
