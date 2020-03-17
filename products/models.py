from django.db import models
from django.db.models import Q
from django.shortcuts import reverse
from django.conf import settings
from django.template.defaultfilters import slugify

from uuid import uuid4

class ProductQuerySet(models.query.QuerySet):
    pass
    
class ProductManager(models.Manager):
    pass

class Product(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    image           = models.ForeignKey(
                		'ItemImage',
                		null=True,
                		blank=True,
                		on_delete=models.SET_NULL
                	)
    featured        = models.BooleanField(default=False)
    quantity        = models.IntegerField(default=0)
    active          = models.BooleanField(default=True)
    is_digital      = models.BooleanField(default=False) # User Library
    timestamp       = models.DateTimeField(auto_now_add=True)
    
    objects = ProductManager()
    
    
    
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