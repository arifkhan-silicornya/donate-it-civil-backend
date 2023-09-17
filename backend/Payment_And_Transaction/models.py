from django.db import models


# file upload directory

def upload_to_payment_doc(instance, filename):
    return 'file/payment/{filename}'.format(filename=filename)



# Models start here

class PaymentMethod(models.Model):
    method_name = models.CharField(max_length=50)

    active= models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.method_name

class CompanyAccount(models.Model):
    payment_method = models.ForeignKey(PaymentMethod,on_delete= models.CASCADE)
    bank_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    account_details = models.TextField(max_length=400)
    bank_img = models.FileField(upload_to=upload_to_payment_doc,blank=True, null=True)
    bar_code = models.FileField(upload_to=upload_to_payment_doc,blank=True, null=True)

    active= models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.bank_name