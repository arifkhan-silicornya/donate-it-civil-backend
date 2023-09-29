from rest_framework import serializers
from IT.models import *
from IT.OrderModel import *
from IT.Payment_Model import *
from Header.models import *
from .serializers import *
from rest_framework.response import Response
from Authentication.serializers import UserSerializer

# =======================         Banner Serializer        ========================

class BannerITSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerIT
        fields= '__all__'

# =======================         Technology Serializer        ========================

class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields= '__all__'
        depth= 1

class TechnologiesCategorySerializer(serializers.ModelSerializer):
    # technology_sections=serializers.SerializerMethodField("get_technology_sections")
    class Meta:
        model = TechnologiesCategory
        fields= '__all__'
        depth = 1

    # def get_technology_sections(self,model):
    #     try:
    #         obj = Technology.objects.filter(category=model,active=True)
    #         seria =  TechnologySerializer(instance=obj,many=True, read_only=True).data
    #         return seria
    #     except:
    #         return []

# =======================         Our Services Serializer         ========================

class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServices
        fields= '__all__'

# =======================         HomeTemplate Serializer         ========================

class HomeTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeTemplate
        fields = '__all__'

# =======================       Home Page HomeTemplate Serializer         ========================
# class UserProfile_Pic_UpdateSerializer(serializers.HyperlinkedModelSerializer):
#     profile_picture = serializers.ImageField(required=False)
#     class Meta:
#         model=User
#         fields = ['profile_picture']
#         expandable_fields = {
#             'profile_picture': ('reviews.ImageSerializer', {'many': True}),
#         }
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
    class Meta:
        model = ProductModel
        fields= '__all__'
        depth = 1


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
        depth = 1
        
        
        
    # --------------------OrderModel serializers----------------------

class OrderItSerializer(serializers.ModelSerializer):
    OrderPdfIT = serializers.SerializerMethodField("get_OrderPdfIT")
    OtherPdfIT = serializers.SerializerMethodField("get_OtherPdfIT")
    user = serializers.SerializerMethodField("get_user")
    ProductIT = serializers.SerializerMethodField("get_ProductIT")
    DeliveryFile = serializers.SerializerMethodField("get_DeliveryFile")
    
    class Meta:
        model = OrderIt
        fields = '__all__'
        include = ['OrderPdfIT','OtherPdfIT','user','ProductIT','DeliveryFile']
    
    def get_OrderPdfIT(self,model):
        try:
            obj = OrderPdfIT.objects.filter(orderit=model)
            seria =  OrderPdfSerializer(instance=obj,many=True, read_only=True).data
            return seria
        except:
            return []
        
    def get_OtherPdfIT(self,model):
        try:
            obj = OtherPdfIT.objects.filter(orderit=model)
            seria =  OtherPdfSerializer(instance=obj,many=True, read_only=True).data
            return seria
        except:
            return []
        
    def get_user(self,model):
        return UserSerializer(User.objects.get(id=model.user.id),many=False).data
    
    def get_ProductIT(self,model):
        return ProductSerializer(ProductModel.objects.get(id=model.ProductIT.id),many=False).data
    
    def get_DeliveryFile(self,model):
        return DeliveryFileSerializer(DeliveryFile.objects.filter(orderit=model.id),many=True).data
    
    
    
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
from Authentication.models import *       
class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'
        depth = 1    
        
# -------------------------login-------------------------

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class GlobalLocSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalLoc
        fields = '__all__'
        
        
class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
        depth = 1
        
class CompanyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAccount
        fields = '__all__'
        depth = 1
        
class BottomBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomBanner
        fields = '__all__'
        depth = 1

class DeliveryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryFile
        fields = '__all__'
        depth = 1
