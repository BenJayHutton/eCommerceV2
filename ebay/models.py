from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.shortcuts import reverse
from accounts.models import User

class EbayAccount(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    production_api_key = models.CharField(max_length=255, blank=True, null= True)
    developer_api_key = models.CharField(max_length=255, blank=True, null= True)
    oath_token = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.full_name
