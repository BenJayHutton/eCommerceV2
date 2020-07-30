from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

from eCommerce.utils import unique_slug_generator
from uuid import uuid4

class ProductQuerySet(models.query.QuerySet): # class.objects.all().attribute
	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True, active=True)

	def search(self, query):
		lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query)|
                   Q(price__icontains=query)|
                   Q(tag__title__icontains=query)
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
		print(product)
		print(id)
		print(quantity)
		if id is not None:
			# look up product by Id
			product = self.get_by_id(id)
			print("product", product)
			
		if product is not None and quantity is not None:
			product.quantity = product.quantity + quantity
			if product.quantity < 0:
				product.quantity = 0
				product.save()
			else:
				product.save()
		print("saved product quantity, new value = ", product.quantity) 

	def decrease_qty_of_product(self, *args, **kwargs):
		product = None
		id = kwargs.get('id')
		quantity = kwargs.get('quantity')
		print(product)
		print(id)
		print(quantity)
		if id is not None:
			# look up product by Id
			product = self.get_by_id(id)
			print("product", product)
			
		if product is not None and quantity is not None:
			product.quantity = product.quantity - quantity
			if product.quantity < 0:
				product.quantity = 0
				product.save()
			else:
				product.save()
		print("saved product quantity, new value = ", product.quantity) 

    

class Product(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    image           = models.ImageField(upload_to='products/', null=True, blank=True)
    featured        = models.BooleanField(default=False)
    quantity        = models.IntegerField(default=0)
    active          = models.BooleanField(default=True)
    is_digital      = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)
    
    objects = ProductManager()
    
    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})
    
    def get_by_id(self, id):
        qs = Product.objects.get(pk=id)
        return qs
        
    def __str__(self):
        return  self.title
    
    
    
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