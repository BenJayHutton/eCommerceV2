from django.conf import settings
from django.contrib.auth.models import (
AbstractBaseUser, BaseUserManager
)
from django.db import models
from django.utils import timezone

class GuestEmail(models.Model):
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class User(AbstractBaseUser):
    email           = models.EmailField()
    full_name       = models.CharField(max_length=255, blank=True, null=True)
    is_guest        = models.BooleanField(default=True)
    is_active       = models.BooleanField(default=True)
    staff           = models.BooleanField(default=False)
    admin           = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class UserBillingAddress(models.Model):
    userprofile = models.ForeignKey(User, on_delete=models.CASCADE)
    is_default  = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.userprofile
    

class UserShippingAddress(models.Model):
    userprofile = models.ForeignKey(User, on_delete=models.CASCADE)
    is_default  = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.userprofile