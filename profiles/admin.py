from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """ User Profile admin """
    list_display = (
        'user',
        'full_name',
        'bio',
        'email_address',
        'creation_date',
        'is_superuser',
    )


admin.site.register(UserProfile, UserProfileAdmin)
