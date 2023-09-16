from django.db import models
from .models import *
from django_resized import ResizedImageField

# Create your models here.

# =======================         Technology Model        ========================

def upload_to_banner(instance, filename):
    return 'image/civil/banner/{filename}'.format(filename=filename)

def upload_to_tech(instance, filename):
    return 'image/civil/technology/{filename}'.format(filename=filename)

def upload_to_service(instance, filename):
    return 'image/civil/service/{filename}'.format(filename=filename)

def upload_to_template(instance, filename):
    return 'image/civil/template/{filename}'.format(filename=filename)

def upload_to_readmore(instance, filename):
    return 'image/civil/readmore/{filename}'.format(filename=filename)

def upload_to_product_img(instance, filename):
    return 'image/civil/product/{filename}'.format(filename=filename)

def upload_to_product(instance, filename):
    return 'file/civil/product/{filename}'.format(filename=filename)

def upload_to_Notice(instance, filename):
    return 'file/civil/notice/{filename}'.format(filename=filename)

def upload_to_Company(instance, filename):
    return 'file/civil/Company/{filename}'.format(filename=filename)

def upload_to_feature_work(instance, filename):
    return 'file/civil/feature_work/{filename}'.format(filename=filename)

def upload_to_architecture(instance, filename):
    return 'file/civil/architecture/{filename}'.format(filename=filename)

def upload_to_bottom_banner(instance, filename):
    return 'file/civil/bottom_banner/{filename}'.format(filename=filename)





# =======================         Banner Model        ========================

class BannerCivil(models.Model):
    title = models.CharField(max_length= 300,blank = False)
    description = models.TextField(blank = False)
    img = ResizedImageField( upload_to=upload_to_banner,blank=True, null=True)
    path = models.CharField(max_length= 300,blank = False,default='/')
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class FeatureWorksCategory(models.Model):
    category = models.CharField(max_length= 300,blank = False)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category)

class FeatureWorks(models.Model):
    category = models.ForeignKey(FeatureWorksCategory, on_delete=models.CASCADE )
    name = models.CharField(max_length= 300,blank = False)
    description = models.TextField(blank = True)
    img = ResizedImageField( upload_to=upload_to_feature_work,blank=True, null=True)
    path = models.CharField(max_length= 300,blank = False, default='/')
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Architecture(models.Model):
    name = models.CharField(max_length= 300,blank = False)
    description = models.TextField(blank = False)
    img = ResizedImageField( upload_to=upload_to_architecture,blank=True, null=True)
    price= models.CharField(max_length=300,blank=False)
    path = models.CharField(max_length= 300,blank = False,default='/')
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

# =======================         Our Services Model        ========================

class OurServices(models.Model):
    name = models.CharField(max_length= 300,blank = False)
    description = models.TextField(blank=True, null=True)
    icon = models.FileField( upload_to=upload_to_service,blank=True, null=True)
    path = models.CharField(max_length= 300,blank = False,default='/')
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)



# =======================         read More Model        ========================

class Readmore(models.Model):
    title = models.CharField(max_length= 300,blank = False)
    description = models.TextField(blank = False)
    img = ResizedImageField(upload_to=upload_to_readmore,blank=True, null=True)
    path = models.CharField(max_length= 300,blank = False,default='/')
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

# =======================         Security Model        ========================

class SecurityPage(models.Model):
    title = models.CharField(max_length= 300,blank = False)
    description = models.TextField(blank = False)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


# =======================     Contact Model        ========================

class Contact(models.Model):
    fullName = models.CharField(max_length= 300,blank = False)
    email = models.EmailField(max_length= 200,blank = False)
    phone_number = models.CharField(max_length= 300,blank = False)
    Company_name = models.CharField(max_length= 300,blank = False)
    website_url = models.CharField(max_length= 300,blank = False)
    
    subject = models.CharField(max_length= 300,blank = False)
    comment = models.TextField(blank = False)

    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)
    
# =======================     Product category Model        ========================
class ProductCategoryModel(models.Model):
    category = models.CharField(max_length= 100,blank = False, null=True)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.category)

# =======================     Product Model        ========================

class ProductModel(models.Model):
    category = models.ForeignKey(ProductCategoryModel,on_delete= models.CASCADE)
    proName = models.CharField(max_length= 100,blank = False)
    proDescription = models.TextField(max_length= 400,blank = True)
    proImg = ResizedImageField( upload_to=upload_to_product_img,blank=True, null=True)
    fileOne = models.FileField( upload_to=upload_to_product,blank=True, null=True)
    fileTwo = models.FileField( upload_to=upload_to_product,blank=True, null=True)
    fileThree = models.FileField( upload_to=upload_to_product,blank=True, null=True)
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.proName)


class NoticeModel(models.Model):
    noticeTitle = models.CharField(max_length= 100,blank = False)
    file = models.FileField( upload_to=upload_to_Notice,blank=True, null=True)
    
    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.noticeTitle)

# =======================     Company Model        ========================

class CompanyModel(models.Model):
    full_Name = models.CharField(max_length= 200,blank = False)
    staff_title = models.CharField(max_length= 200,blank = False)
    staff_img = ResizedImageField( upload_to=upload_to_Company,blank=True, null=True)
    email = models.EmailField(max_length= 200,blank = False)
    mobileNumber = models.CharField(max_length= 200,blank = False)
    home_address = models.TextField(max_length= 300, blank = True)

    active=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.full_Name)+ " " + str(self.staff_title)


class BottomBanner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=700)
    img = ResizedImageField( upload_to=upload_to_bottom_banner,blank=True, null=True)
    link = models.TextField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class GlobalLocation(models.Model):
    country = models.CharField(max_length=50)
    office_address = models.TextField(max_length=200)
    email = models.EmailField(max_length=100 )
    contact_no = models.CharField(max_length=200)

    active= models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email