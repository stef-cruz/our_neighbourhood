from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    """ Events admin """
    list_display = (
        'user',
        'title',
        'description',
        'event_date',
        'event_time',
        'event_price',
        'event_contact',
        'event_category',
        'creation_date',
    )


admin.site.register(Event, EventAdmin)
