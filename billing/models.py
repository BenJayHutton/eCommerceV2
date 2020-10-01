from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.urls import reverse


from accounts.models import GuestEmail
User = settings.AUTH_USER_MODEL

import stripe

STRIPE_SECRET_API_KEY = getattr(settings, "STRIPE_SECRET_API_KEY", None)
stripe.api_key = STRIPE_SECRET_API_KEY



class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        guest_email_id = request.session.get('guest_email_id')
        created = False
        obj = None
        if user.is_authenticated:
            obj, created = self.model.objects.get_or_create(user=user, email=user.email)
        elif guest_email_id is not None:
            guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
            obj, created = self.model.objects.get_or_create(email=guest_email_obj.email)
        else:
            pass
        return obj, created
    
class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=120, null=True, blank=True)
    
    objects = BillingProfileManager()
    
    def __str__(self):
        return self.email

    def charge(self, order_obj, card=None):
        return Charge.objects.do(self, order_obj, card)

    def get_cards(self):
        return self.card_set.all()

    @property
    def has_card(self): # instance.has_card
        card_qs = self.get_cards()
        return card_qs.exists()
    
    @property
    def default_card(self):
        default_cards = self.get_cards().filter(default=True)
        if default_cards.exists():
            return default_cards.first()
        return None

def billing_profile_created_reciever(sender, instance, *args, **kwargs):
    if not instance.customer_id and instance.email:
        print("sending to stripe to create profile")
        customer = stripe.Customer.create(
            email = instance.email
        )
        print(customer)
        instance.customer_id = customer.id

        
pre_save.connect(billing_profile_created_reciever, sender=BillingProfile)

def user_created_reciever(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(user_created_reciever, sender=User)

class CardManager(models.Manager):
    def add_new(self, billing_profile, token):
        if token:
            customer = stripe.Customer.retrieve(billing_profile.customer_id)
            stripe_card_response = customer.sources.create(source=token)
        if str(stripe_card_response.object) =="card":
            new_card_obj = self.model(
                billing_profile=billing_profile,
                stripe_id = stripe_card_response.id,
                brand = stripe_card_response.brand,
                country = stripe_card_response.country,
                exp_month = stripe_card_response.exp_month,
                exp_year = stripe_card_response.exp_year,
                last4 = stripe_card_response.last4
            )
            new_card_obj.save()
            return new_card_obj
        return None
        

class Card(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    stripe_id       = models.CharField(max_length=120)
    brand           = models.CharField(max_length=120, null=True, blank=True)
    country         = models.CharField(max_length=20, null=True, blank=True)
    exp_month       = models.IntegerField(null=True, blank=True)
    exp_year        = models.IntegerField(null=True, blank=True)
    last4           = models.CharField(max_length=4, null=True, blank=True)
    default         = models.BooleanField(default=True)

    objects = CardManager()

    def __str__(self):
        return "{} {}".format(self.brand, self.last4)

class ChargeManager(models.Manager):
    def do(self, billing_profile, order_obj, card=None):
        card_obj = card
        if card_obj is None:
            cards = billing_profile.card_set.filter(default=True)
            if cards.exists():
                card_obj = cards.first()
        if card_obj is None:
            return False, "No cards available"

        c = stripe.Charge.create(
            amount = int(order_obj.total * 100),
            currency = "gbp",
            customer = billing_profile.customer_id,
            source = card_obj.stripe_id,
            metadata={"Order_id: ": order_obj.order_id},
        )
        print(c)
        new_charge_obj = self.model(
            billing_profile = billing_profile,
            stripe_id       = c.id,
            paid            = c.paid,
            refunded        = c.refunded,
            outcome         = c.outcome,
            outcome_type    = c.outcome['type'],
            seller_message  = c.outcome.get('seller_message'),
            risk_level      = c.outcome.get('risk_level'),
        )
        new_charge_obj.save()
        return new_charge_obj.paid, new_charge_obj.seller_message


class Charge(models.Model):
    billing_profile = models.ForeignKey(BillingProfile,on_delete=models.CASCADE)
    stripe_id       = models.CharField(max_length=120)
    paid            = models.BooleanField(default=False)
    refunded        = models.BooleanField(default=False)
    outcome         = models.TextField(null=True, blank=True)
    outcome_type    = models.CharField(max_length=120, null=True, blank=True)
    seller_message  = models.CharField(max_length=120, null=True, blank=True)
    risk_level      = models.CharField(max_length=120, null=True, blank=True)

    objects = ChargeManager()