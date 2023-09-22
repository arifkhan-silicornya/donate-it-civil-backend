from rest_framework import serializers
from Header.models import *
from Civil.models import *
from Header.serializers import *
from Authentication.models import *


# =======================         Navbar Serializer         ========================

class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields= '__all__'


# =======================         SiteList Serializer         ========================
class SiteSerializer(serializers.ModelSerializer):
    navbar_sections=serializers.SerializerMethodField("get_navbar_sections")

    class Meta:
        model = siteList
        fields= ['id','name','baseroot','img', 'active','created_at','last_update_at','navbar_sections']
    
    def get_navbar_sections(self,model):
        try:
            obj = Navbar.objects.filter(site=model,active=True)
            seria =  NavbarSerializer(instance=obj,many=True, read_only=True)
            return seria.data
        except:
            return []
        

# =======================         Banner Serializer        ========================

class BannerCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerCivil
        fields= '__all__'
        # fields= ['title','description','img','path']

# =======================         FeatureWorks Serializer        ========================

class FeatureWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureWorks
        fields= '__all__'
        # fields= ['name','description','path','img']

class FeatureWorksCategoryeSerializer(serializers.ModelSerializer):
    FeatureWorks =serializers.SerializerMethodField("get_FeatureWorks")
    class Meta:
        model = FeatureWorksCategory
        fields= ['id','category','active','created_at','last_update_at','FeatureWorks']

    def get_FeatureWorks(self,model):
        try:
            obj = FeatureWorks.objects.filter(category=model,active=True)
            seria =  FeatureWorksSerializer(instance=obj,many=True, read_only=True).data
            return seria
        except:
            return []


# =======================         Architecture Serializer         ========================

class ArchitectureSerializer(serializers.ModelSerializer):
    Details =serializers.SerializerMethodField("get_deatial_feature")
    class Meta:
        model = Architecture
        # fields= '__all__'
        fields= ['id','name','description','path','img','price','active', 'Details']

    def get_deatial_feature(self,model):
        try:
            if DetailsOfFeatureDesign.objects.filter(Architecture=model).exists():
                return True
            else:
                return False
        except:
            return False    

# =======================         Our Services Serializer         ========================

class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields= '__all__'
        # fields= ['name','description','path','icon']


# =======================       Home Page HomeTemplate Readmore Serializer         ========================

class ReadmoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Readmore
        fields= '__all__'
        # fields= ['title','description','path','img']

# =======================       Security Page Serializer         ========================

class SecurityPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityPage
        fields= '__all__'
        # fields= ['title','description']


# =======================       Contact Page Serializer         ========================

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields= '__all__'


# =======================       Product category Serializer         ========================

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategoryModel
        fields= '__all__'
        # fields= ['id','proName','proDescription','proImg','fileOne','fileTwo','fileThree']

# =======================       Product Model Serializer         ========================

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields= '__all__'
        # fields= ['id','proName','proDescription','proImg','fileOne','fileTwo','fileThree']


# =======================       Notice Model Serializer         ========================

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeModel
        fields= '__all__'
        # fields= ['noticeTitle','file','created_at']

# =======================       Company Model Serializer         ========================

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields= '__all__'
        # fields= ['full_Name','staff_title','home_address','email','mobileNumber','staff_img']

# =======================       BottomBanner Model Serializer         ========================

class BottomBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomBanner
        fields= '__all__'

# =======================       GlobalLocation Model Serializer         ========================

class GlobalLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalLocation
        fields= '__all__'

# =======================       GlobalLocation Model Serializer         ========================

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude=['password']
        # fields= '__all__'


# =======================       DetailsOfFeatureDesign Model Serializer         ========================

class DetailsOfFeatureDesignSerializer(serializers.ModelSerializer):
    Architecture_name = serializers.SerializerMethodField("get_architecture_name")
    Architecture = serializers.SerializerMethodField("get_architecture")
    class Meta:
        model = DetailsOfFeatureDesign
        fields= ['id', 'bed', 'bath', 'kitchen', 'Plan_description', 'active', 'Architecture_name', 'Architecture']
        # fields= '__all__'

    def get_architecture_name(self, model):
        return model.Architecture.name
        
    def get_architecture(self, model):
        return model.Architecture.id    

# =======================       ImagesOfDetailsDesign Model Serializer         ========================

class ImagesOfDetailsDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesOfDetailsDesign
        fields= '__all__'

   