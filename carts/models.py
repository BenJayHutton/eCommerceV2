from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

from products.models import Product

User = settings.AUTH_USER_MODEL

class CartItemManager(models.Manager):
    def create_cart_item(self,*args, **kwargs):
        '''
        TODO: 
        '''
        product_id = kwargs.get('product_id')
        product_quantity = int(kwargs.get('product_quantity'))
        item_price = None
        total = None
        cart_item_obj = None

        if product_id is not None and product_quantity > 0:
            product_obj = Product().get_by_id(product_id)
            item_price = float(product_obj.price)
            total = item_price * product_quantity
            cart_item_obj = self.model.objects.create(product=product_obj, quantity=product_quantity, price_of_item=item_price, total=total)

            print("product: ", product_obj)
            print("qty: ", product_quantity)
            print("product price: ", item_price)
            print("total price: ", total)
            print("cart_item_obj: ", cart_item_obj.product.title)          

        return cart_item_obj

class CartItem(models.Model):
    product         = models.ForeignKey(Product, default=None, blank=True, on_delete=models.CASCADE)
    quantity        = models.IntegerField(default=0, null=True)
    price_of_item   = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)
    total           = models.DecimalField(default=0.00, max_digits=20, decimal_places=2)

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

class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    cart_items    = models.ManyToManyField(CartItem, default=None, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def pre_save_cart_reciever(sender, instance, action, *args, **kwargs):
    if action =='post_add' or action=='post_remove' or action =='post_clear':
        cart_items = instance.cart_items.all()
        total = 0
        for x in cart_items:
            total += x.total
        if instance.subtotal != total:
            instance.subtotal = total
            instance.total = total
            instance.save()

m2m_changed.connect(pre_save_cart_reciever, sender=Cart.cart_items.through)