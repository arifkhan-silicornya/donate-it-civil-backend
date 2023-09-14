from rest_framework import serializers
from .models import *
from Header.models import *
from .serializers import *

# =======================         Banner Serializer        ========================

class BannerITSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerIT
        fields= ['title','description','img','path']

# =======================         Technology Serializer        ========================

class TechnologySerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('get_category')
    class Meta:
        model = Technology
        fields= '__all__'
    def get_category(self,model):
        return model.category.category
    
class TechnologiesCategorySerializer(serializers.ModelSerializer):
    technology_sections=serializers.SerializerMethodField("get_technology_sections")
    class Meta:
        model = TechnologiesCategory
        fields= ['category','technology_sections']

    def get_technology_sections(self,model):
        try:
            obj = Technology.objects.filter(category=model,active=True)
            seria =  TechnologySerializer(instance=obj,many=True, read_only=True).data
            return seria
        except:
            return []

# =======================         Our Services Serializer         ========================

class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields= '__all__'

# =======================         HomeTemplate Serializer         ========================

class HomeTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTemplate
        fields= '__all__'

# =======================       Home Page HomeTemplate Serializer         ========================

class ReadmoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readmore
        fields= '__all__'

# =======================       Security Page Serializer         ========================

class SecurityPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityPage
        fields= '__all__'


# =======================       Contact Page Serializer         ========================

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields= '__all__'


# =======================       Product Model Serializer         ========================

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField('get_category')
    class Meta:
        model = ProductModel 
        fields= ['id','proName','proDescription','proImg','fileOne','fileTwo','fileThree','category_name']
        depth = 1

    def get_category(self,model):
        return model.category.category


class ProductCategoryModelSerializer(serializers.ModelSerializer):
    Products =serializers.SerializerMethodField("get_Product")
    class Meta:
        model = ProductCategoryModel
        fields= ['category','Products']
        depth = 1

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
        fields= '__all__'

# =======================       Notice Model Serializer         ========================

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields= '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields = '__all__'
        
class BottomBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomBanner
        fields = '__all__'

class GlobalLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalLocation
        fields = '__all__'
    
