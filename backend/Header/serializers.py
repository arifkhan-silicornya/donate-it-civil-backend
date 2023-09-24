from rest_framework import serializers
from .models import *
from Header.models import *
from .serializers import *


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields= ['name','baseroot','site','icon']


class SiteSerializer(serializers.ModelSerializer):
    navbar_sections=serializers.SerializerMethodField("get_navbar_sections")

    class Meta:
        model = siteList
        fields= ['id', 'name','baseroot','img','navbar_sections']
    
    def get_navbar_sections(self,model):
        try:
            obj = Navbar.objects.filter(site=model,active=True)
            seria =  NavbarSerializer(instance=obj,many=True, read_only=True)
            return seria.data
        except:
            return []
    
# new brand logo
class DonateBrandLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateBrandLogo
        fields= ['name','img']

class ITBrandLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITBrandLogo
        fields= ['name','img']

class CivilBrandLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CivilBrandLogo
        fields= ['name','img']

