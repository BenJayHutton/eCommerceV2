from django.conf import settings
from django.db import models
from accounts.models import User
from orders.models import Order

User = settings.AUTH_USER_MODEL

class Payment(models.Model):
    user = models.ForeignKey(User,default=None, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    paymentMethod = models.CharField(max_length=128)
    paypalOrderID = models.CharField(max_length=128)
    paypalPayerID = models.CharField(max_length=128)
    is_paid = models.BooleanField(default=False)
    summery = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  "Order: " +self.order.order_id


        total = body["total"]
        vat = body["vat"]
        shipping = body["shipping"]
        subTotal = body["subTotal"]
        paypalOrderID = body["paypalOrderID"]
        paypalPayerID = body["paypalPayerID"]
