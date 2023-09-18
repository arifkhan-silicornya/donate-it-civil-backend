from django.db import models
from .OrderModel import OrderIt
from Authentication.models import User

# file upload directory

def upload_to_payment_doc(instance, filename):
    return 'image/it/payment/bank_img/{filename}'.format(filename=filename)

def upload_to_bar_code(instance, filename):
    return 'image/it/payment/bar_code/{filename}'.format(filename=filename)

def upload_to_Pay_Receipt(instance, filename):
    return 'image/it/payment/Receipt/{filename}'.format(filename=filename)



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
    bar_code = models.FileField(upload_to=upload_to_bar_code,blank=True, null=True)

    active= models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.bank_name

class TransactionModel(models.Model):
    bank = models.ForeignKey(CompanyAccount,on_delete= models.SET_NULL, null=True)
    user = models.ForeignKey(User,on_delete= models.SET_NULL, null=True)
    order = models.ForeignKey(OrderIt,on_delete= models.SET_NULL, null=True)

    amount = models.PositiveIntegerField(blank=False, null=False)
    Transaction_id = models.CharField(max_length=200)
    account_Info = models.TextField(max_length=500)
    acc_holder_mail = models.EmailField(max_length=50)
    acc_holder_phone = models.IntegerField()

    pay_receipt_doc = models.FileField(upload_to=upload_to_Pay_Receipt,blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Transaction_id
    