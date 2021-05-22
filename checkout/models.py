from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    """
    A model to record payments
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=50, blank=False, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
