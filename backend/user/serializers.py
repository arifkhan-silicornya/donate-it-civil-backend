from rest_framework import serializers
from Authentication.models import *

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        exclude=['password','email','username']

class UserProfile_Pic_UpdateSerializer(serializers.HyperlinkedModelSerializer):
    profile_picture = serializers.ImageField(required=False)
    class Meta:
        model=User
        fields = ['profile_picture']
        expandable_fields = {
            'profile_picture': ('reviews.ImageSerializer', {'many': True}),
        }
