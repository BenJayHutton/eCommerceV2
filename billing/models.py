from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.urls import reverse

User = settings.AUTH_USER_MODEL
    
class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=120, null=True, blank=True)
    
    def __str__(self):
        return self.email


# def billing_profile_created_reciever(sender, instance, created, *args, **kwargs):
#     if created:
#         print("sending to stripe to create profile")
#         instance.customer_id = newID
#         instance.save

def user_created_reciever(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_reciever, sender=User)
