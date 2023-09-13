# Authentication.serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    # followers=serializers.SerializerMethodField("getfollowers")
    # followings=serializers.SerializerMethodField("getfollowings")
    # friends=serializers.SerializerMethodField("getfriends")
    # isReseller=serializers.SerializerMethodField("getIsReseller")
    # userLevel=serializers.SerializerMethodField("getUserLevel")
    class Meta:
        model=User
        exclude=['password']
    # def getfollowers(self,model:models.User):
    #     followers=Follow.objects.filter(
    #         Q(active=True) & Q(follow_to=model)
    #     )
    #     return FollowSerializer(followers,many=True).data
    # def getfollowings(self,model:models.User):
    #     followings=Follow.objects.filter(
    #         Q(active=True) & Q(user=model)
    #     )
    #     return FollowSerializer(followings,many=True).data
    # def getIsReseller(self,model):
    #     return Reseller.objects.filter(user=model).exists()
    # def getUserLevel(self,model):
    #     try:
    #         return UserLevelSerializer(model.user_level).data
    #     except:
    #         return None
    
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
        fields = ['username', 'email','first_name','last_name','countryName', 'password','confirm_password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        password = data.get('password')
        confirm_password = data.pop('confirm_password', None)

        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")

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
            raise serializers.ValidationError("New passwords do not match.")
        return data

    def update(self, instance, validated_data):
        user = instance
        old_password = validated_data['old_password']
        new_password = validated_data['new_password']

        if not user.check_password(old_password):
            raise serializers.ValidationError("Invalid old password.")

        user.set_password(new_password)
        user.save()
        return user
        
