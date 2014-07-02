# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse

from mptt.models import MPTTModel, TreeForeignKey
import mptt



class Category(MPTTModel):
    name = models.CharField('Название', max_length=50, unique=True)
    parent = mptt.fields.TreeForeignKey('self', null=True, blank=True,
                                         related_name='children')
    
    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category_details', args=[str(self.id)])
    
    def get_products_list(self):
        return Product.objects.filter(category=self.id)
    
    
    
class Product(models.Model):
    category = models.ForeignKey(Category)
    
    name = models.CharField('Название', max_length=50, unique=True)
    #image = models.ImageField(upload_to='images')
    url = models.CharField('Ссылка на сайт производителя', max_length=128, blank=True)
    description = models.TextField(blank=True)
    

    def __unicode__(self):
        return self.name