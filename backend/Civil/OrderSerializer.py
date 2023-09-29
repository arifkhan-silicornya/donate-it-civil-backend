from rest_framework import serializers
from .models import *
from .OrderModel import *
from django.db.models import Q

    # --------------------OrderModel serializers----------------------

class CreateOrderCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCivil
        fields = '__all__'

class OrderCivilSerializer(serializers.ModelSerializer):
    OrderPdfCivil=serializers.SerializerMethodField("get_OrderPdfCivil")
    OtherPdfCivil=serializers.SerializerMethodField("get_OtherPdfCivil")
    PersonalInfoCivil=serializers.SerializerMethodField("get_PersonalInfoCivil")
    PresentAddressCivil=serializers.SerializerMethodField("get_PresentAddressCivil")
    PermanentAddressCivil=serializers.SerializerMethodField("get_PermanentAddressCivil")
    CompanyDetail=serializers.SerializerMethodField("get_CompanyDetail")
    Contact_info=serializers.SerializerMethodField("get_Contact_info")
    SocialMediaLink=serializers.SerializerMethodField("get_SocialMediaLink")
    DeliveryFile = serializers.SerializerMethodField("get_DeliveryFile")
    class Meta:
        model = OrderCivil
        fields = '__all__'
        depth = 1
    
    def get_OrderPdfCivil(self,model:OrderCivil):
        try:
            OrderPdf=OrderPdfCivil.objects.filter(Q(OrderCivil=model))
            return OrderPdfSerializer(OrderPdf,many=True).data
        except:
            return []
    
    def get_OtherPdfCivil(self,model:OrderCivil):
        try:
            OtherPdf=OtherPdfCivil.objects.filter(Q(OrderCivil=model))
            return OtherPdfSerializer(OtherPdf,many=True).data
        except:
            return []
    def get_PersonalInfoCivil(self,model:OrderCivil):
        try:
            PersonalInfo=PersonalInfoCivil.objects.filter(Q(OrderCivil=model))
            return PersonalInfoSerializer(PersonalInfo,many=True).data
        except:
            return []
    def get_PresentAddressCivil(self,model:OrderCivil):
        try:
            PresentAddress=PresentAddressCivil.objects.filter(Q(OrderCivil=model))
            return PresentAddressSerializer(PresentAddress,many=True).data
        except:
            return []
    def get_PermanentAddressCivil(self,model:OrderCivil):
        try:
            PermanentAddress=PermanentAddressCivil.objects.filter(Q(OrderCivil=model))
            return PermanentAddressSerializer(PermanentAddress,many=True).data
        except:
            return []
    def get_CompanyDetail(self,model:OrderCivil):
        try:
            CompanyDe=CompanyDetailCivil.objects.filter(Q(OrderCivil=model))
            return CompanyDetailSerializer(CompanyDe,many=True).data
        except:
            return []
    def get_Contact_info(self,model:OrderCivil):
        try:
            Contact_info=Contact_infoCivil.objects.filter(Q(OrderCivil=model))
            return Contact_infoSerializer(Contact_info,many=True).data
        except:
            return []
    def get_SocialMediaLink(self,model:OrderCivil):
        try:
            SocialMediaLink=SocialMediaLinkCivil.objects.filter(Q(OrderCivil=model))
            return SocialMediaLinkSerializer(SocialMediaLink,many=True).data
        except:
            return []
    def get_DeliveryFile(self,model):
        return DeliveryFileCivilSerializer(DeliveryFileCivil.objects.filter(ordercivil=model.id),many=True).data

class DeliveryFileCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryFileCivil
        fields = ['id','file','create_at','update_at']
        depth = 1
        
class OrderPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPdfCivil
        fields = '__all__'
        depth = 1
        
class OtherPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPdfCivil
        fields = '__all__'
        depth = 1
        
class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfoCivil
        fields = '__all__'
        depth = 1
        
class PresentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentAddressCivil
        fields = '__all__'
        depth = 1
class PermanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentAddressCivil
        fields = '__all__'
        depth = 1
        
        
class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetailCivil
        fields = '__all__'
        depth = 1
        
        
class Contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_infoCivil
        fields = '__all__'
        depth = 1
        
class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLinkCivil
        fields = '__all__'
        depth = 1

