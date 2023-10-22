from rest_framework import serializers
from Civil.Payment_Model import *

# =======================         Payment Serializer        ========================



    
class CompanyAccount_Serializer(serializers.ModelSerializer):
    method_name = serializers.SerializerMethodField("get_payment_method")
    method_name_id = serializers.SerializerMethodField("get_payment_method_id")
    class Meta:
        model = CompanyAccount
        fields= ['id', 'bank_name','country' , 'account_details' ,'bank_img','bar_code','method_name','method_name_id','active']
        depth = 1

    def get_payment_method(self,model):
        return  model.payment_method.method_name
    def get_payment_method_id(self,model):
        return  model.payment_method.id
            


class PaymentMethodSerializer(serializers.ModelSerializer):
    CompanyAccount = serializers.SerializerMethodField("get_CompanyAccount")
    class Meta:
        model = PaymentMethod
        fields= ['id', 'method_name','CompanyAccount', 'active']

    def get_CompanyAccount(self,model):
        try:
            obj = CompanyAccount.objects.filter(payment_method=model,active=True)
            return CompanyAccount_Serializer(instance=obj,many=True, read_only=True).data
        except:
            return {}

