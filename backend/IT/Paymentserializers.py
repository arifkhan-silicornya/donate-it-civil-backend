from rest_framework import serializers
from .Payment_Model import *

# =======================         Payment Serializer        ========================



    
class CompanyAccount_Serializer(serializers.ModelSerializer):
    method_name = serializers.SerializerMethodField("get_payment_method")
    class Meta:
        model = CompanyAccount
        fields= ['id', 'bank_name','country' , 'account_details' ,'bank_img','bar_code','method_name']
        depth = 1

    def get_payment_method(self,model):
        return  model.payment_method.method_name
            


class PaymentMethodSerializer(serializers.ModelSerializer):
    CompanyAccount = serializers.SerializerMethodField("get_CompanyAccount")
    class Meta:
        model = PaymentMethod
        fields= ['method_name','CompanyAccount']

    def get_CompanyAccount(self,model):
        try:
            obj = CompanyAccount.objects.filter(payment_method=model,active=True)
            seria =  CompanyAccount_Serializer(instance=obj,many=True, read_only=True).data
            return seria
        except:
            return {}

class TransactionModel_Serializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField("get_user")
    bank = serializers.SerializerMethodField("get_bank")
    class Meta:
        model = TransactionModel
        fields= ['id','amount', 'Transaction_id', 'account_Info' , 'acc_holder_mail' , 'acc_holder_phone', 'pay_receipt_doc', 'user' , 'order', 'bank','created_at']

    def get_user(self,model):
        return  model.user.username
    
    def get_bank(self,model):
        return  model.bank.bank_name 