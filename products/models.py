from __future__ import unicode_literals
from django.db import models
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.title, filename)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    #slug = models.SlugField()
    slug = AutoSlugField(populate_from='title', unique=True)    # from autoslug
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['title']
    
    def __unicode__(self):
        return self.title
        
    @property    
    def get_price(self):
		return self.price
        
    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.slug])    # kwargs={"slug": self.slug}
    