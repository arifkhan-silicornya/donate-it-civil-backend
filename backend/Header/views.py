from django.shortcuts import render
from .serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *

# Create your views here.
class HeaderSerializerViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = siteList.objects.filter(active=True)
    serializer_class = SiteSerializer
