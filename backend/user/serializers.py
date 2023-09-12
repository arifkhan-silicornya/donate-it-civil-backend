from rest_framework import serializers
from Authentication.models import *

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(required=False)
    class Meta:
        model=User
        # fields="__all__"
        expandable_fields = {
            'profile_picture': ('reviews.ImageSerializer', {'many': True}),
        }
        exclude=['password','email','username']