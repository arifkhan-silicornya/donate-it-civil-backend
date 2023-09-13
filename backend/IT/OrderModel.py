from django.db import models
from .models import ProductModel
from django_resized import ResizedImageField
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
    project_description = models.TextField(max_length= 300, null = True)
    
    total_price = models.CharField(max_length= 300, null = True)
    total_online_paid = models.CharField(max_length= 300, null = True)

    status =(
    ("pen", "Pending"),
    ("Pay", "Payment"),
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
        return str(self.user.id)

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
    is_same = models.BooleanField(default=True)
    GENDER_CHOICES =(
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
    )

    Title_CHOICES =(
    ("Mr", "Mr"),
    ("Mrs", "Mrs"),
    ("Ms", "Ms"),
    ("Miss", "Miss"),
    ("Dr", "Dr"),
    ("Engr", "Engr"),
    ("Master", "Master"),
    )

    gender=models.CharField(max_length=7,choices=GENDER_CHOICES,null=True)
    title=models.CharField(max_length=7,choices=Title_CHOICES,null=True)
    date_of_birth=models.DateField(null=True)
    occupation=models.CharField(max_length=10,null=True,blank=True)

    first_name = models.CharField(max_length= 300,null = True)
    last_name = models.CharField(max_length= 300,null = True)
    
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)

# =========================       Present Address       =====================
class PresentAddressIT(models.Model):
    orderit = models.OneToOneField(OrderIt, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=True)
    country = models.CharField(max_length= 300,null = True)
    State = models.CharField(max_length= 300,null = True)
    city = models.CharField(max_length= 300,null = True)
    houseRoad = models.CharField(max_length= 300,null = True)
    zipCode = models.CharField(max_length= 300,null = True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)

# =========================       Permanent Address       =====================
class PermanentAddressIT(models.Model):
    orderit = models.OneToOneField(OrderIt, on_delete=models.CASCADE )
    is_same_as_user = models.BooleanField(default=False)
    is_same_present_address = models.BooleanField(default=False,null=True)
    country = models.CharField(max_length= 300,null = True)
    State = models.CharField(max_length= 300,null = True)
    city = models.CharField(max_length= 300,null = True)
    houseRoad = models.CharField(max_length= 300,null = True)
    zipCode = models.CharField(max_length= 300,null = True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)

# =========================       Company Details       =====================

class CompanyDetailIT(models.Model):
    orderit = models.OneToOneField(OrderIt, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=True)
    Company_same = models.CharField(max_length= 300,null = False)

    Com_type =(
    ("Pr", "Private"),
    ("Pu", "Public"),
    ("O", "Others"),
    )

    Company_type = models.CharField(max_length=7,choices=Com_type,null=True)
    Company_location = models.CharField(max_length= 300,null = True)
    Company_website_url = models.URLField(max_length= 300,null = True)

    Company_phone_dial_code = models.CharField(max_length= 300,null = True)
    Company_phone_number = models.CharField(max_length= 300,null = True)
    Company_email = models.CharField(max_length= 300,null = True)
    Company_details = models.TextField(max_length= 300,null = True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)


# =========================       Contact Info       =====================

class Contact_infoIT(models.Model):
    orderit = models.OneToOneField(OrderIt, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=True)
    
    personal_phone_dial_code = models.CharField(max_length= 300,null = True)
    personal_phone_number = models.CharField(max_length= 300,null = True)
    home_phone_dial_code = models.CharField(max_length= 300,null = True)
    home_phone_number = models.CharField(max_length= 300,null = True)

    contact_email = models.EmailField(max_length= 300,null = True)
    contact_address = models.TextField(max_length= 300,null = True)


    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)


# =========================       Social Media Link       =====================

class SocialMediaLinkIT(models.Model):
    orderit = models.ForeignKey(OrderIt, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=True)
    
    name = models.CharField(max_length= 300,null = True)
    link = models.CharField(max_length= 300,null = True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.orderit.id)
