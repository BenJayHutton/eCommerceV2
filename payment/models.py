from django.contrib.auth import get_user_model
from django.db import models
from orders.models import Order
from accounts.models import User
# User = get_user_model()


class Payment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    paymentMethod = models.CharField(max_length=128)
    paypalOrderID = models.CharField(max_length=128)
    paypalPayerID = models.CharField(max_length=128)
    is_paid = models.BooleanField(default=False)
    summery = models.TextField()
    total = models.FloatField(default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  "Order: " + self.order.order_id
