from django.contrib.auth import get_user_model
from django.db import models
from orders.models import Order
from accounts.models import User

PAYMENT_METHOD = (
    ('None', 'None'),
    ('Cash', 'Cash'),
    ('Cheque', 'Cheque'),
    ('BACS', 'BACS'),
    ('Paypal', 'Paypal'),
    ('Stripe', 'Stripe')
)


class PaypalPaymentMethod(models.Model):
    paypalOrderID   = models.CharField(max_length=128)
    paypalPayerID   = models.CharField(max_length=128)

    def __str__(self):
        return "Paypal payment id: " + self.paypalOrderID

class StripePaymentMethod(models.Model):
    stripe_id   = models.CharField(max_length=120)
    brand       = models.CharField(max_length=120, null=True, blank=True)
    country     = models.CharField(max_length=20, null=True, blank=True)
    exp_month   = models.IntegerField(null=True, blank=True)
    exp_year    = models.IntegerField(null=True, blank=True)
    last4       = models.CharField(max_length=4, null=True, blank=True)
    default     = models.BooleanField(default=True)
    active      = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Stripe payment id: " + self.stripe_id

class Payment(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    paypal_forign_key = models.ForeignKey(PaypalPaymentMethod, blank=True, null=True, on_delete=models.SET_NULL)
    stripe_forign_key = models.ForeignKey(StripePaymentMethod, blank=True, null=True, on_delete=models.SET_NULL)
    paymentMethod = models.CharField(max_length=12, choices=PAYMENT_METHOD, default="None")
    is_paid = models.BooleanField(default=False)
    summery = models.TextField()
    total = models.FloatField(default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.user.email + ": " + "Paid by: " + self.paymentMethod + " order: " + self.order.order_id
