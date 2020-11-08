from django.conf import settings
import decimal
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

from eCommerce.utils import unique_slug_generator, get_filename
from uuid import uuid4

class ProductQuerySet(models.query.QuerySet): # class.objects.all().attribute
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query)|
                   Q(price__icontains=query)
                   #Q(tag__title__icontains=query)
                   )
        return self.filter(lookups)

class ProductManager(models.Manager):
    #overriding get_queryset so we can use the queryset above
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None
    
    def search(self, query):
        return self.get_queryset().active().search(query)

    def increase_qty_of_product(self, *args, **kwargs):
        product = None
        id = kwargs.get('id')
        quantity = kwargs.get('quantity')
        if id is not None:
            product = self.get_by_id(id)
            
        if product is not None and quantity is not None:
            product.quantity = product.quantity + quantity
            if product.quantity < 0:
                product.quantity = 0
                product.save()
            else:
                product.save()

    def decrease_qty_of_product(self, *args, **kwargs):
        product = None
        id = kwargs.get('id')
        quantity = kwargs.get('quantity')
        if id is not None:
            product = self.get_by_id(id)
            
        if product is not None and quantity is not None:
            product.quantity = product.quantity - quantity
            if product.quantity < 0:
                product.quantity = 0
                product.save()
            else:
                product.save()


class Product(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)
    vat             = models.DecimalField(max_digits=10, decimal_places=2,  default=0.00)
    image           = models.ImageField(upload_to='products/', null=True, blank=True)
    featured        = models.BooleanField(default=False)
    quantity        = models.IntegerField(default=0)
    active          = models.BooleanField(default=True)
    is_digital      = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)
    
    objects = ProductManager()
    
    def has_quantity(self):
        return self.quantity > 0

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})
    
    def get_by_id(self, id):
        qs = Product.objects.get(pk=id)
        return qs
        
    def __str__(self):
        return  self.title

    @property
    def name(self):
        return self.title

    def get_downloads(self):
        qs = self.productfile_set.all()
        return qs
    
def product_pre_save_reciever(sender, instance, *args, **kwargs):
    instance.vat = instance.price * decimal.Decimal(0.2)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    

pre_save.connect(product_pre_save_reciever, sender=Product)


def upload_product_file_loc(instance, filename):
    slug = instance.product.slug
    if not slug:
        slug = unique_slug_generator(instance.product)
    location = "product/{}/".format(slug)
    return location + filename


class ProductFile(models.Model):
    product         = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    file            = models.FileField(upload_to=upload_product_file_loc, storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
    free            = models.BooleanField(default=False)
    user_required   = models.BooleanField(default=False)

    def __str__(self):
        return str(self.file.name)
    
    def get_default_url(self):
        return self.product.get_absolute_url()

    def get_download_url(self):
        return reverse("products:download", kwargs={"slug": self.product.slug, "pk": self.pk})

    @property
    def name(self):
        return get_filename(self.file.name)


class ItemImage(models.Model):
    upload_date = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField(
        upload_to='item-images/'
    )
    items = models.ManyToManyField(
        Product
    )

    def __str__(self):
        return str(self.upload_date)


class ItemTag(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True
    )
    public = models.BooleanField(
        default=False
    )
    items = models.ManyToManyField(
        Product,
        blank=True
    )
    blurb = models.CharField(
        max_length = 500,
        null = True
    )

    def __str__(self):
        return self.name