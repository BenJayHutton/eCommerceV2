from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.db.models.signals import pre_save, post_save, m2m_changed
from products.models import Product
from accounts.models import User
# User = get_user_model()

class CartItemManagerQuerySet(models.query.QuerySet):
    def update_total(self):
        return self.aggregate(Sum("total"))


class CartItemManager(models.Manager):
    def get_queryset(self):
        return CartItemManagerQuerySet(self.model, using=self._db)

    def new_or_get(self, request, *args, **kwargs):
        if not request.session.exists(request.session.session_key):
            request.session.create()
        cart_item_id = request.session.get("cart_item_id", None)
        session_id = request.session.session_key
        product_obj = kwargs.get("product_obj", None)
        product_quantity = kwargs.get("product_quantity", None)
        qs = self.get_queryset().filter(id=cart_item_id, product=product_obj)
        if qs:
            cart_item_obj = qs.first()
            new_item_obj = False
            if product_obj and cart_item_obj.product is None:
                cart_item_obj.product = product_obj
                cart_item_obj.save()
            if product_quantity:
                cart_item_obj.quantity = product_quantity
                cart_item_obj.save()
        else:
            cart_item_obj = CartItem.objects.create(session_id=session_id, quantity=product_quantity, product=product_obj)
            if product_obj and cart_item_obj.product is None:
                cart_item_obj.product = product_obj
                cart_item_obj.save()
            new_item_obj = True
            request.session['cart_item_id'] = cart_item_obj.id
        return cart_item_obj, new_item_obj
            

class CartItem(models.Model):
    product         = models.ForeignKey(Product, default=None, null=True, blank=True, on_delete=models.SET_NULL)
    quantity        = models.IntegerField(default=None, null=True)
    price_of_item   = models.FloatField(default=0.00)
    session_id      = models.CharField(max_length=120, default=0, null=True, blank=True)
    total           = models.FloatField(default=0.00)

    objects = CartItemManager()

    def __str__(self):
        return str(self.id)


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            cart_obj = qs.first()
            new_obj = False
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)

    def calculate_cart_total(self, request, *args, **kwargs):
        cart_obj = kwargs.get("cart_obj", None)
        total = 0
        vat_total = 0
        sub_total = 0
        for x in cart_obj.cart_items.all():
            total += x.total
        vat_total = total * 0.2
        sub_total = total + vat_total
        return total, vat_total, sub_total


class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    cart_items  = models.ManyToManyField(CartItem, default=None, blank=True)
    total       = models.FloatField(default=0.00)
    vat_total   = models.FloatField(default=0.00)
    subtotal    = models.FloatField(default=0.00)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    @property
    def is_digital(self):
        qs = self.cart_items.all()
        for x in qs:
            if not x.product.is_digital:
                return False
        return True


def cart_item_pre_save_reciever(sender, instance, *args, **kwargs):
    try:
        quantity = int(instance.quantity)
    except:
        quantity = 0
    try:
        price_of_item = instance.product.price
    except:
        price_of_item = 0

    instance.price_of_item = price_of_item
    instance.total = quantity * price_of_item


pre_save.connect(cart_item_pre_save_reciever, sender=CartItem)


def cart_post_save_reciever(sender, instance, *args, **kwargs):
    cart_items = instance.cart_items.all()
    vat_total = 0
    sub_total = 0
    cart_item_total = cart_items.update_total()['total__sum']
    if cart_item_total is None:
        cart_item_total = 0
    vat_total = cart_item_total * 0.2
    sub_total = cart_item_total + vat_total
    instance.total = cart_item_total
    instance.vat_total = vat_total
    instance.subtotal = sub_total


post_save.connect(cart_post_save_reciever, sender=Cart)
    
    
def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        vat_total = 0
        sub_total = 0
        cart_items = instance.cart_items.all()
        cart_item_total = cart_items.update_total()['total__sum']
        if cart_item_total is None:
            cart_item_total = 0
        vat_total = cart_item_total * 0.2
        sub_total = cart_item_total + vat_total
        instance.total = cart_item_total
        instance.vat_total = vat_total
        instance.subtotal = sub_total
        instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.cart_items.through)
