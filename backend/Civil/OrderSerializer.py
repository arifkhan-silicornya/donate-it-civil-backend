from rest_framework import serializers
from .models import *
from .OrderModel import *


    # --------------------OrderModel serializers----------------------

class OrderCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCivil
        fields = '__all__'
        depth = 1
        
class OrderPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPdfCivil
        fields = '__all__'
        depth = 1
        
class OtherPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPdfCivil
        fields = '__all__'
        depth = 1
        
class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfoCivil
        fields = '__all__'
        depth = 1
        
class PresentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentAddressCivil
        fields = '__all__'
        depth = 1
class PermanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentAddressCivil
        fields = '__all__'
        depth = 1
        
        
class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetailCivil
        fields = '__all__'
        depth = 1
        
        
class Contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_infoCivil
        fields = '__all__'
        depth = 1
        
class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinkCivil
        fields = '__all__'
        depth = 1
        