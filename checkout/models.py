from django.db import models

from profiles.models import UserProfile


class Order(models.Model):
    """
    A model to record orders. One user can place multiple orders.
    """
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, related_name='orders')
    amount = models.CharField(max_length=50, blank=False, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
