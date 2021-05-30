from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Events admin """
    list_display = (
        'contact_category',
        'contact_name',
        'contact_email',
        'message',
        'is_resolved',
        'creation_date'
    )

admin.site.register(Contact, ContactAdmin)
