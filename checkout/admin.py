from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    """ Order admin """
    list_display = (
        'user',
        'amount',
        'payment_date',
    )


admin.site.register(Order, OrderAdmin)
