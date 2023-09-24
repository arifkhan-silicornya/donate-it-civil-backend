from rest_framework import serializers
from Header.models import *


class siteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = siteList
        fields = '__all__'
        
        
class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'
        depth = 1

#brand Logo
class ITBrandLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITBrandLogo
        fields = '__all__'