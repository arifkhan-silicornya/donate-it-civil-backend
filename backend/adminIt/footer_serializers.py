from rest_framework import serializers
from footer.models import *

class footerSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerSection
        fields = '__all__'
        depth = 1
        
        
class footerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerItem
        fields = '__all__'
        depth = 1
        
class footerHeadOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerHeadOffice
        fields = '__all__'
        depth = 1
        
        
class footerSocialIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerSocialIcon
        fields = '__all__'
        depth = 1
        
        
class PaymentIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentIcon
        fields = '__all__'
        depth = 1
                
class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = '__all__'
        