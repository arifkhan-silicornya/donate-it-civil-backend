from django.db import models
from Header.models import siteList
from django_resized import ResizedImageField

# Create your models here.

def upload_to_icons(instance, filename):
    return 'image/icons/{filename}'.format(filename=filename)

class footerSection(models.Model):
    site = models.ForeignKey(siteList, on_delete=models.CASCADE )
    title = models.CharField(max_length= 300,blank = False)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.site.name) + " " + str(self.title)


def order_id():
    n = 0
    try:
        FI = footerItem.objects.filter().count()
        return FI+1
    except:
        n+1


class footerItem(models.Model):
    footerSection = models.ForeignKey(footerSection, on_delete=models.CASCADE )
    name = models.CharField(max_length= 300,blank = False)
    description = models.TextField(max_length= 1000,blank = True,null=True)
    link = models.CharField(max_length= 300,blank = False,default='/')
    order = models.CharField(max_length= 300,blank = True,default= order_id)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.footerSection.title) + " " + str(self.name)

class footerHeadOffice(models.Model):
    siteList = models.ForeignKey(siteList, on_delete=models.CASCADE )
    usa_address = models.CharField(max_length= 300,blank = True,null=True)
    usa_email = models.EmailField(max_length= 300,blank = True,null=True)
    usa_phone = models.CharField(max_length= 300,blank = True,null=True)
    usa_fax = models.CharField(max_length= 300,blank = True,null=True)
    uk_address = models.CharField(max_length= 300,blank = True,null=True)
    uk_email = models.EmailField(max_length= 300,blank = True,null=True)
    uk_phone = models.CharField(max_length= 300,blank = True,null=True)
    uk_fax = models.CharField(max_length= 300,blank = True,null=True)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.usa_address) + " " +str(self.uk_address)

class footerSocialIcon(models.Model):
    siteList = models.ForeignKey(siteList, on_delete=models.CASCADE)
    name = models.CharField(max_length= 300,blank = False)
    link = models.URLField(max_length= 300,blank = False)
    
    icon = ResizedImageField( upload_to=upload_to_icons,blank=True, null=True,)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.name) + " " +str(self.active)

class PaymentIcon(models.Model):
    name = models.CharField(max_length= 300,blank = False)
    
    icon = ResizedImageField( upload_to=upload_to_icons,blank=True, null=True,)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.name) + " " +str(self.active)


class NewsLetter(models.Model):
    email = models.EmailField(max_length= 300,blank = False)
    
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  str(self.email) + " " +str(self.active)