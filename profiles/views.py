from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


@login_required(login_url='login')
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
            messages.error(request, 'Something went wrong, please try again')
    else:
        form = UserProfileForm(instance=profile)
    # TODO: events = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'form': form,
        # 'events': events,
    }
    return render(request, template, context)


@login_required(login_url='login')
def delete_profile(request, user):
    """ A view to delete current user"""

    if not request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.user.username == user:
        user = request.user
        user.delete()

    return redirect(reverse('home'))
