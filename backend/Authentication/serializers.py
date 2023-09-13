# Authentication.serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *
from django.db.models import Q
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    Education=serializers.SerializerMethodField("get_education")
    SocialMediaLink=serializers.SerializerMethodField("get_SocialMediaLink")
    CompanyDetail=serializers.SerializerMethodField("get_CompanyDetail")
    ContactInfo=serializers.SerializerMethodField("get_ContactInfo")
    PresentAddress=serializers.SerializerMethodField("get_PresentAddress")
    PermanentAddress=serializers.SerializerMethodField("get_PermanentAddress")
    class Meta:
        model=User
        exclude=['password']

    def get_education(self,model:User):
        try:
            Education=EducationalQualification.objects.filter(Q(user=model))
            return EducationalQualificationSerializer(Education,many=True).data
        except:
            return []
    
    def get_CompanyDetail(self,model:User):
        try:
            Company =CompanyDetail.objects.filter(Q(user=model))
            return CompanyDetailSerializer(Company,many=True).data
        except:
            return []
        
    def get_ContactInfo(self,model:User):
        try:
            Company =Contact_info.objects.filter(Q(user=model))
            return Contact_infoSerializer(Company,many=True).data
        except:
            return []
    
    def get_PresentAddress(self,model:User):
        try:
            Present =PresentAddress.objects.filter(Q(user=model))
            return PresentAddressSerializer(Present,many=True).data
        except:
            return []
    
    def get_PermanentAddress(self,model:User):
        try:
            Permanent = PermanentAddress.objects.filter(Q(user=model))
            return PermanentAddressSerializer(Permanent,many=True).data
        except:
            return []
    
    def get_SocialMediaLink(self,model:User):
        try:
            social_media=SocialMediaLink.objects.filter(active=True,user=model)
            return SocialMediaLinkSerializer(social_media,many=True).data
        except:
            return []
    
    
    # def get_CompanyDetail(self,model):
    #     try:
    #         return CompanyDetailSerializer(model.user).data
    #     except:
    #         return None
    
    # def getIsReseller(self,model):
    #     return Reseller.objects.filter(user=model).exists()
    # def getfriends(self,model:models.User):
    #     followings=Follow.objects.filter(
    #         Q(active=True) & Q(user=model)
    #     )
    #     followers=Follow.objects.filter(
    #         Q(active=True) & Q(follow_to=model)
    #     )
    #     friends=[]
    #     if( followings.exists() and followers.exists() ):
    #         for f in followers:
    #             any=followings.filter(follow_to=f.user)
    #             if any.exists():
    #                 friends.append(any[0])
    #     return FollowSerializer(friends,many=True).data

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email','countryName', 'password','confirm_password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)

        return data
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password:
            instance.set_password(password)
        instance.save()

        return instance

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class CodeVerificationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True)
    class Meta:
        model = CodeVerification
        fields = ['email', 'code']

    def validate(self, data):
        email = data.get('email')

        if User.objects.filter(email=email).exists():
            user_obj = User.objects.get(email=email)
            return user_obj
        else:
            raise serializers.ValidationError("User not found")


class GenerateCodeSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True)
    class Meta:
        model = CodeVerification
        fields = ['email']


class ResetPasswordSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['email','code','new_password','confirm_password']
        extra_kwargs = {'new_password': {'write_only': True}}
    
    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("passwords do not match.")
        return data

    def update(self, instance, validated_data):
        user = instance
        email = validated_data['email']
       
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid user.")
        
        code = validated_data['code']
        new_password = validated_data['new_password']

        # Validate the code against the database
        try:
            Code_obj = CodeVerification.objects.get(user=user_obj, code=code)
        except CodeVerification.DoesNotExist:
            raise serializers.ValidationError("Invalid code.")

        # If the code is valid, update the user's password
        currentDT = x.strftime("%x %X")
        if(currentDT > Code_obj.expiredDate ) :
            raise serializers.ValidationError("Code Expired. Verify in 15 minite. try again!!!")
        else:
            user_obj.set_password(new_password)
            user_obj.save()
            return user
        


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['email','code','new_password','confirm_password']
        extra_kwargs = {'new_password': {'write_only': True}}
    
    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"type":"error","msg":"New passwords do not match."})
        return data

    def update(self, instance, validated_data):
        user = instance
        old_password = validated_data['old_password']
        new_password = validated_data['new_password']

        if not user.check_password(old_password):
            raise serializers.ValidationError({"type":"error","msg":"Invalid old password."})

        user.set_password(new_password)
        user.save()
        return user
        

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
 

class EducationalQualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalQualification
        fields = '__all__'

class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'

class CompanyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetail
        fields = '__all__'

class PresentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentAddress
        fields = '__all__'

class PermanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermanentAddress
        fields = '__all__'

class Contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_info
        fields = '__all__'

class User_SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'

