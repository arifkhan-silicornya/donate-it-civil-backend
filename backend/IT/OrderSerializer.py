from rest_framework import serializers
from .models import *
from .OrderModel import *


    # --------------------OrderModel serializers----------------------

class OrderItSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderIt
        fields = '__all__'
        depth = 1
        
class OrderPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPdfIT
        fields = '__all__'
        depth = 1
        
class OtherPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPdfIT
        fields = '__all__'
        depth = 1
        
class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfoIT
        fields = '__all__'
        depth = 1
        
class PresentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentAddressIT
        fields = '__all__'
        depth = 1
class PermanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentAddressIT
        fields = '__all__'
        depth = 1
        
        
class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetailIT
        fields = '__all__'
        depth = 1
        
        
class Contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_infoIT
        fields = '__all__'
        depth = 1
        
class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinkIT
        fields = '__all__'
        depth = 1
        