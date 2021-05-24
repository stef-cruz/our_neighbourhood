from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    """ Events admin """
    list_display = (
        'is_paid',
        'user',
        'title',
        'description',
        'event_date',
        'event_time',
        'event_location',
        'event_price',
        'event_contact',
        'event_category',
        'creation_date',
    )


admin.site.register(Event, EventAdmin)
