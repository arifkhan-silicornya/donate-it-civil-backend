from rest_framework import serializers
from .models import *
from Header.models import *
from .serializers import *

# =======================         Banner Serializer        ========================

class BannerCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerCivil
        fields= ['title','description','img','path']

# =======================         FeatureWorks Serializer        ========================

class FeatureWorksSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category')
    class Meta:
        model = FeatureWorks
        # fields= ['name','description','path','img']
        fields= ['category_name','name','description','path','img']


class FeatureWorksCategoryerializer(serializers.ModelSerializer):
    FeatureWorks =serializers.SerializerMethodField("get_FeatureWorks")
    class Meta:
        model = FeatureWorksCategory
        fields= ['category','FeatureWorks']

    def get_FeatureWorks(self,model):
        try:
            obj = FeatureWorks.objects.filter(category=model,active=True)
            seria =  FeatureWorksSerializer(instance=obj, many=True, read_only=True).data
            return seria
        except:
            return []


# =======================         Architecture Serializer         ========================

class ArchitectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Architecture
        fields= ['name','description','path','img','price']

# =======================         Our Services Serializer         ========================

class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields= ['name','description','path','icon']



# =======================       Home Page HomeTemplate Serializer         ========================

class ReadmoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readmore
        fields= ['title','description','path','img']

# =======================       Security Page Serializer         ========================

class SecurityPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityPage
        fields= ['title','description']


# =======================       Contact Page Serializer         ========================

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields= '__all__'


# =======================       Product Model Serializer         ========================

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel 
        fields= ['id','proName','proDescription','proImg','fileOne','fileTwo','fileThree']

class ProductCategoryModelSerializer(serializers.ModelSerializer):
    Products =serializers.SerializerMethodField("get_Product")
    class Meta:
        model = ProductCategoryModel
        fields= ['category','Products']

    def get_Product(self,model):
        try:
            obj = ProductModel.objects.filter(category=model,active=True)
            seria =  ProductSerializer(instance=obj,many=True, read_only=True).data
            return seria
        except:
            return []
# =======================       Notice Model Serializer         ========================

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeModel
        fields= ['noticeTitle','file','created_at']

# =======================       Notice Model Serializer         ========================

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields= ['full_Name','staff_title','home_address','email','mobileNumber','staff_img']

