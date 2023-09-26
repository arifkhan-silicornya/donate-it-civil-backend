from django.db import models
from .models import *
from django_resized import ResizedImageField

# Create your models here.
def upload_to_site(instance, filename):
    return 'image/site/{filename}'.format(filename=filename)

def upload_to_icons(instance, filename):
    return 'image/icons/{filename}'.format(filename=filename)
  
class siteList(models.Model):
    name = models.CharField(max_length= 300,blank = False)
    baseroot = models.CharField(max_length= 300,blank = False,default='/')
    img = ResizedImageField( upload_to=upload_to_site,blank=True, null=True,)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) 

class Navbar(models.Model):
    site = models.ForeignKey(siteList, on_delete=models.CASCADE )
    name = models.CharField(max_length= 300,blank = False)
    baseroot = models.CharField(max_length= 300,blank = False,default='/')
    icon = ResizedImageField(size=(30, 30), upload_to=upload_to_icons,blank=True, null=True,)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name) +" "+ str(self.site)

# Brand Logo for donate
class DonateBrandLogo(models.Model):
    name = models.CharField(max_length= 30,blank=True, null=True)
    img = ResizedImageField( upload_to=upload_to_site,blank=True, null=True)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

# Brand Logo for donate
class ITBrandLogo(models.Model):
    name = models.CharField(max_length= 30,blank=True, null=True)
    img = ResizedImageField( upload_to=upload_to_site,blank=True, null=True,)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

# Brand Logo for donate
class CivilBrandLogo(models.Model):
    name = models.CharField(max_length= 30,blank=True, null=True)
    img = ResizedImageField( upload_to=upload_to_site,blank=True, null=True,)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)