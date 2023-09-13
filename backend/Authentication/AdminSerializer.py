from rest_framework import serializers

# -------------------------login-------------------------

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)