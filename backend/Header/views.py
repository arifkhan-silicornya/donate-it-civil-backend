from django.shortcuts import render
from .serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *

# Create your views here.
class HeaderView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        site = siteList.objects.get(name='IT')
        site_serializer = SiteSerializer(site).data
        navbar = Navbar.objects.filter(site=site_serializer['id'],active=True)
        navbar_serializer = NavbarSerializer(navbar, many=True, context={'request':request}).data
        return Response({'navbar': navbar_serializer})