from rest_framework import serializers
from Civil.models import *
from Civil.OrderModel import *


# --------------------OrderModel serializers----------------------

# =======================         OrderCivil Serializer         ========================

class OrderCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCivil
        fields = '__all__'
        depth = 1


# =======================         OrderPdfCivil Serializer         ========================        
class OrderPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPdfCivil
        fields = '__all__'
        depth = 1
        

# =======================         OtherPdfCivil Serializer         ========================          
class OtherPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPdfCivil
        fields = '__all__'
        depth = 1


# =======================         PersonalInfoCivil Serializer         ========================           
class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfoCivil
        fields = '__all__'
        depth = 1
        
# =======================         PresentAddressCivil Serializer         ========================         
class PresentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentAddressCivil
        fields = '__all__'
        depth = 1


# =======================         PermanentAddressCivil Serializer         ========================         
class PermanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentAddressCivil
        fields = '__all__'
        depth = 1
        

# =======================         CompanyDetailCivil Serializer         ========================         
class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetailCivil
        fields = '__all__'
        depth = 1
        

# =======================         Contact_infoCivil Serializer         ========================         
class Contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_infoCivil
        fields = '__all__'
        depth = 1


# =======================         SocialMediaLinkCivil Serializer         ========================         
class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinkCivil
        fields = '__all__'
        depth = 1
        