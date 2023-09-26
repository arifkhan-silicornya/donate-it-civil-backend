from django.db import models
from .models import ProductModel
from Authentication.models import User

# file upload directory

def upload_to_OrderPdf(instance, filename):
    return 'image/it/OrderPdf/{filename}'.format(filename=filename)

def upload_to_OtherPdf(instance, filename):
    return 'image/it/OtherPdf/{filename}'.format(filename=filename)


# Models start here

# =========================       Order Model       =====================
class OrderIt(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ProductIT = models.ForeignKey(ProductModel ,  on_delete=models.PROTECT)
    currency = models.CharField(max_length= 300, null = False)
    project_description = models.TextField(max_length= 1000, null = True,blank=True)
    
    payment_left = models.PositiveIntegerField(default=2)
    total_price = models.BigIntegerField(default=0, null = True,blank=True)
    total_online_paid = models.BigIntegerField(default=0, null = True,blank=True)
    total_offline_paid = models.BigIntegerField(default=0, null = True,blank=True)

    status =(
    ("pen", "Pending"),
    ("pay", "Payment"),
    ("can", "Canceled"),
    ("wor", "Working"),
    ("com", "Completed"),
    ("del", "Delivery"),
    )

    status = models.CharField(max_length=7,choices=status,null=False,default='pen')

    delivery_date_from = models.DateField( null = True)
    delivery_date_to = models.DateField( null = True)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.id)

# =========================       Order Pdf       =====================

class OrderPdfIT(models.Model):
    orderit = models.ForeignKey(OrderIt, on_delete=models.CASCADE )
    
    file = models.FileField( upload_to=upload_to_OrderPdf,blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)

# =========================       Other Pdf       =====================

class OtherPdfIT(models.Model):
    orderit = models.ForeignKey(OrderIt, on_delete=models.CASCADE )
    file = models.FileField( upload_to=upload_to_OtherPdf,blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)



# =========================       Personal Info       =====================
class PersonalInfoIT(models.Model):
    orderit = models.OneToOneField(OrderIt, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=True,null=False,blank=False)
    GENDER_CHOICES =(
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
    )

    
    gender=models.CharField(max_length=7,choices=GENDER_CHOICES,null=True,blank=True)
    title=models.CharField(max_length=7,null=True,blank=True)
    date_of_birth=models.CharField(max_length=30,null=True,blank=True)
    occupation=models.CharField(max_length=10,null=True,blank=True)

    first_name = models.CharField(max_length= 300,null=True,blank=True)
    last_name = models.CharField(max_length= 300,null=True,blank=True)
    
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)

# =========================       Present Address       =====================
class PresentAddressIT(models.Model):
    orderit = models.OneToOneField(OrderIt, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=True,null=False,blank=False)
    country = models.CharField(max_length= 300,null=True,blank=True)
    State = models.CharField(max_length= 300,null=True,blank=True)
    city = models.CharField(max_length= 300,null=True,blank=True)
    houseRoad = models.CharField(max_length= 300,null=True,blank=True)
    zipCode = models.CharField(max_length= 300,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)

# =========================       Permanent Address       =====================
class PermanentAddressIT(models.Model):
    orderit = models.OneToOneField(OrderIt, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=True,null=False,blank=False)
    address = models.TextField(max_length= 300,null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)

# =========================       Company Details       =====================

class CompanyDetailIT(models.Model):
    orderit = models.OneToOneField(OrderIt, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=True)
    Company_same = models.CharField(max_length= 300,null=True,blank=True)

    Com_type =(
    ("Pr", "Private"),
    ("Pu", "Public"),
    ("O", "Others"),
    )

    Company_type = models.CharField(max_length=30,choices=Com_type,null=True,blank=True)
    Company_location = models.CharField(max_length= 300,null=True,blank=True)
    Company_website_url = models.URLField(max_length= 100,null=True,blank=True)

    Company_phone_dial_code = models.CharField(max_length= 8,null=True,blank=True)
    Company_phone_number = models.CharField(max_length= 30,null=True,blank=True)
    Company_email = models.EmailField(max_length= 50,null=True,blank=True)
    Company_details = models.TextField(max_length= 300,null=True,blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id) +" com id :"+ str(self.id)


# =========================       Contact Info       =====================

class Contact_infoIT(models.Model):
    orderit = models.OneToOneField(OrderIt, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=True)
    
    personal_phone_dial_code = models.CharField(max_length= 300,null=True,blank=True)
    personal_phone_number = models.CharField(max_length= 300,null=True,blank=True)
    home_phone_dial_code = models.CharField(max_length= 300,null=True,blank=True)
    home_phone_number = models.CharField(max_length= 300,null=True,blank=True)

    contact_email = models.EmailField(max_length= 300,null=True,blank=True)
    contact_address = models.TextField(max_length= 300,null=True,blank=True)


    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)


# =========================       Social Media Link       =====================

class SocialMediaLinkIT(models.Model):
    orderit = models.ForeignKey(OrderIt, on_delete=models.CASCADE )
    
    name = models.CharField(max_length= 300,null=True,blank=True)
    link = models.CharField(max_length= 300,null=True,blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id) + " " + str(self.id)


    # =========================       Delivery File       =====================

class DeliveryFile(models.Model):
    orderit = models.ForeignKey(OrderIt, on_delete=models.SET_NULL,null=True )
    
    file = models.FileField( upload_to=upload_to_OrderPdf,blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.id)