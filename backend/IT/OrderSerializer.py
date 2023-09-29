from rest_framework import serializers
from .models import *
from .OrderModel import *
from django.db.models import Q
from Authentication.serializers import UserSerializer


    # --------------------OrderModel serializers----------------------

class CreateOrderItSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderIt
        fields = '__all__'

class OrderItSerializer(serializers.ModelSerializer): 
    OrderPdfIT=serializers.SerializerMethodField("get_OrderPdfIT")
    OtherPdfIT=serializers.SerializerMethodField("get_OtherPdfIT")
    PersonalInfoIT=serializers.SerializerMethodField("get_PersonalInfoIT")
    PresentAddressIT=serializers.SerializerMethodField("get_PresentAddressIT")
    PermanentAddressIT=serializers.SerializerMethodField("get_PermanentAddressIT")
    CompanyDetail=serializers.SerializerMethodField("get_CompanyDetail")
    Contact_info=serializers.SerializerMethodField("get_Contact_info")
    SocialMediaLink=serializers.SerializerMethodField("get_SocialMediaLink")
    DeliveryFile = serializers.SerializerMethodField("get_DeliveryFile")
    class Meta:
        model = OrderIt
        fields = '__all__'
        depth = 1
    
    def get_OrderPdfIT(self,model:OrderIt):
        try:
            OrderPdf=OrderPdfIT.objects.filter(Q(orderit=model))
            return OrderPdfSerializer(OrderPdf,many=True).data
        except:
            return []
    
    def get_OtherPdfIT(self,model:OrderIt):
        try:
            OtherPdf=OtherPdfIT.objects.filter(Q(orderit=model))
            return OtherPdfSerializer(OtherPdf,many=True).data
        except:
            return []
    def get_PersonalInfoIT(self,model:OrderIt):
        try:
            PersonalInfo=PersonalInfoIT.objects.filter(Q(orderit=model))
            return PersonalInfoSerializer(PersonalInfo,many=True).data
        except:
            return []
    def get_PresentAddressIT(self,model:OrderIt):
        try:
            PresentAddress=PresentAddressIT.objects.filter(Q(orderit=model))
            return PresentAddressSerializer(PresentAddress,many=True).data
        except:
            return []
    def get_PermanentAddressIT(self,model:OrderIt):
        try:
            PermanentAddress=PermanentAddressIT.objects.filter(Q(orderit=model))
            return PermanentAddressSerializer(PermanentAddress,many=True).data
        except:
            return []
    def get_CompanyDetail(self,model:OrderIt):
        try:
            CompanyDe=CompanyDetailIT.objects.filter(Q(orderit=model))
            return CompanyDetailSerializer(CompanyDe,many=True).data
        except:
            return []
    def get_Contact_info(self,model:OrderIt):
        try:
            Contact_info=Contact_infoIT.objects.filter(Q(orderit=model))
            return Contact_infoSerializer(Contact_info,many=True).data
        except:
            return []
    def get_SocialMediaLink(self,model:OrderIt):
        try:
            SocialMediaLink=SocialMediaLinkIT.objects.filter(Q(orderit=model))
            return SocialMediaLinkSerializer(SocialMediaLink,many=True).data
        except:
            return []
    def get_DeliveryFile(self,model):
        return DeliveryFileSerializer(DeliveryFile.objects.filter(orderit=model.id),many=True).data

class DeliveryFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryFile
        fields = ['id','file','create_at','update_at']
        depth = 1

class OrderPdfSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    class Meta:
        model = OrderPdfIT
        fields = ['file']
        depth = 1
        
class OtherPdfSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False)
    class Meta:
        model = OtherPdfIT
        fields = ['file']
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
        fields = ['name','link']
        depth = 1
        