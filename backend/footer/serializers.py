from rest_framework import serializers
from .models import *
from Header.models import *
from .serializers import *

class FooterSocialIconSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerSocialIcon
        fields= ['name','link','icon']


class FooterItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerItem
        fields= ['name','description','link','order']

class footerHeadOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerHeadOffice
        fields= ['usa_address','usa_email','usa_phone','usa_fax','uk_address','uk_email','uk_phone','uk_fax']


class FooterSectionSerializer(serializers.ModelSerializer):

    
    footer_items=serializers.SerializerMethodField("get_footer_items")
    

    class Meta:
        model = footerSection
        fields= ['title','footer_items']
    
    def get_footer_items(self,model):
        try:
            obj = footerItem.objects.filter(footerSection=model,active=True)
            seria = FooterItemSerializer(instance=obj,many=True, read_only=True)
            return seria.data
        except:
            return []


class PaymentIconSerializer(serializers.ModelSerializer):

    class Meta:
        model = PaymentIcon
        fields= ['name','icon']


class FooterSerializer(serializers.ModelSerializer):
    footer_sections=serializers.SerializerMethodField("get_footer_sections")
    payment_sections=serializers.SerializerMethodField("get_payment_sections")
    footer_item_HeadOffice=serializers.SerializerMethodField("get_footer_item_HeadOffice")
    
    footer_social_icons=serializers.SerializerMethodField("get_footer_social_icons")

    class Meta:
        model = siteList
        fields= ['name','footer_sections','payment_sections','footer_item_HeadOffice','footer_social_icons']
    
    def get_footer_sections(self,model):
        try:
            obj = footerSection.objects.filter(site=model,active=True)
            seria =  FooterSectionSerializer(instance=obj,many=True, read_only=True)
            return seria.data
        except:
            return []
        
    def get_payment_sections(self,model):
        try:
            obj = PaymentIcon.objects.filter(active=True)
            seria =  PaymentIconSerializer(instance=obj,many=True, read_only=True)
            return seria.data
        except:
            return []
          
    def get_footer_item_HeadOffice(self,model):
        obj = footerHeadOffice.objects.filter(siteList =  model,active=True)
        seria = footerHeadOfficeSerializer(instance=obj,many=True, read_only=True)
        return seria.data
    
        
    def get_footer_social_icons(self,model):
        try:
            obj = footerSocialIcon.objects.filter(siteList=model,active=True)
            seria=  FooterSocialIconSerializer(instance=obj,many=True, read_only=True)
            return seria.data
        except:
            return []  
        


# NewsLetter
class NewsLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsLetter
        fields= '__all__'
        
        
class FooterItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerItem
        fields = '__all__'
        
class FooterSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerSection
        fields = '__all__'
        
class FooterHeadOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = footerHeadOffice
        fields = '__all__'
