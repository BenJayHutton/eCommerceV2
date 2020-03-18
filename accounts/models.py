from django.conf import settings
from django.contrib.auth.models import (
AbstractBaseUser, BaseUserManager
)
from django.db import models
from django.utils import timezone

class UserManagerQuerySet(models.query.QuerySet):
    pass

class UserManager(BaseUserManager):
    pass
    
class User(AbstractBaseUser):
    email = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    full_name       = models.CharField(max_length=255, blank=True, null=True)
    is_guest        = models.BooleanField(default=True)
    is_active       = models.BooleanField(default=True)
    staff           = models.BooleanField(default=False)
    admin           = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def __str__(self):
        return self.email
        





class UserBillingAddressQuerySet(models.query.QuerySet):
    pass

class UserBillingAddressManager(models.Manager):
    pass
    
class UserBillingAddress(models.Model):
    userprofile = models.ForeignKey(User, on_delete=models.CASCADE)
    is_default  = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    
    objects = UserBillingAddressManager()
    
    def __str__(self):
        return self.userprofile
    






class UserShippingAddressQuerySet(models.query.QuerySet):
    pass

class UserShippingAddressManager(models.Manager):
    pass
            
class UserShippingAddress(models.Model):
    userprofile = models.ForeignKey(User, on_delete=models.CASCADE)
    is_default  = models.BooleanField(default=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    
    objects = UserShippingAddressManager()
    
    def __str__(self):
        return self.userprofile