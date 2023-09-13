from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,PermissionsMixin, User, UserManager)
import datetime

# Create your models here.

x = datetime.datetime.now()
x2 = datetime.datetime.now() + datetime.timedelta(minutes=15)


def upload_to_profile(instance, filename):
    return 'image/profile/{filename}'.format(filename=filename)


class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError('user should have a username')
        if email is None:
            raise TypeError('User should have a Email')
        
        user=self.model(username=username,email=self.normalize_email(email),password=None)
        user.set_password(password)
        user.save()       
        return user
        
    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError('User should have a password')
        
        user=self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.is_verified = True
        user.save()         
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=255,unique=True,db_index=True,null=False)
    email = models.EmailField(max_length=255,unique=True,db_index=True,null=False)
    first_name = models.CharField(max_length=255,null=True)
    last_name = models.CharField(max_length=255,null=True)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_agent=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

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



    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,null=True)
    title=models.CharField(max_length=28,choices=Title_CHOICES,null=True)
    date_of_birth=models.DateField(null=True)
    father_name=models.CharField(max_length=100,null=True,blank=True)
    mother_name=models.CharField(max_length=100,null=True,blank=True)
    marital_status=models.CharField(max_length=100,null=True,blank=True)
    blood_group=models.CharField(max_length=10,null=True,blank=True)
    occupation=models.CharField(max_length=100,null=True,blank=True)
    PhoneDialCode=models.CharField(max_length=15,null=True,blank=True)
    countryName=models.CharField(max_length=100,null=True,blank=True)
    phoneNumber=models.CharField(max_length=20,null=True,blank=True)
    
    profile_picture=ResizedImageField( upload_to=upload_to_profile,blank=True, null=True,)
    def __str__(self) :
        return self.email +" "+str(self.id) +" "+self.username

# =========================       code verification       =====================

class CodeVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    code = models.CharField(max_length= 300,blank = False)
    status = models.CharField(max_length= 300,blank = False,default=0)
    createDate = models.CharField(max_length= 300,blank = False,default=x.strftime("%x %X"))
    expiredDate = models.CharField(max_length= 300,blank = False,default=x2.strftime("%x %X"))

    def __str__(self):
        return str(self.user.id)

# =========================       Present Address       =====================
class PresentAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    country = models.CharField(max_length= 300,null = False)
    State = models.CharField(max_length= 300,null = False)
    city = models.CharField(max_length= 300,null = False)
    houseRoad = models.CharField(max_length= 300,null = False)
    zipCode = models.CharField(max_length= 300,null = False)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user.id)

# =========================       Permanent Address       =====================
class PermanentAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    is_same = models.BooleanField(default=False,null=True)
    country = models.CharField(max_length= 300,null = True)
    State = models.CharField(max_length= 300,null = True)
    city = models.CharField(max_length= 300,null = True)
    houseRoad = models.CharField(max_length= 300,null = True)
    zipCode = models.CharField(max_length= 300,null = True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user.id)

# =========================       Company Details       =====================

class CompanyDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    Company_same = models.CharField(max_length= 300,null = False)

    Com_type =(
    ("Pr", "Private"),
    ("Pu", "Public"),
    ("O", "Others"),
    )

    Company_type = models.CharField(max_length=7,choices=Com_type,null=False)
    Company_location = models.CharField(max_length= 300,null = True)
    Company_website_url = models.URLField(max_length= 300,null = True)

    Company_phone_dial_code = models.CharField(max_length= 300,null = False)
    Company_phone_number = models.CharField(max_length= 300,null = False)
    Company_email = models.CharField(max_length= 300,null = False)
    Company_details = models.TextField(max_length= 300,null = True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user.id)


# =========================       Contact Info       =====================

class Contact_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    
    personal_phone_dial_code = models.CharField(max_length= 300,null = False)
    personal_phone_number = models.CharField(max_length= 300,null = False)
    home_phone_dial_code = models.CharField(max_length= 300,null = False)
    home_phone_number = models.CharField(max_length= 300,null = False)

    contact_email = models.EmailField(max_length= 300,null = False)
    contact_address = models.TextField(max_length= 300,null = True)


    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user.id)


# =========================       Social Media Link       =====================

class SocialMediaLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    
    name = models.CharField(max_length= 300,null = False)
    link = models.CharField(max_length= 300,null = False)

    active=models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.user.username)
    
class EducationalQualification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    institute = models.CharField(max_length=250, null=True)
    degree_name = models.CharField(max_length= 300,null = True)
    course_name = models.CharField(max_length= 300,null = True)
    from_year = models.CharField(max_length= 300,null = True)
    to_year = models.CharField(max_length= 300,null = True)
    grade = models.CharField(max_length= 300,null = True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now= True)

    def __str__(self):
        return str(self.institute)

