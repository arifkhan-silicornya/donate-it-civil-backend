from django.shortcuts import render
from .serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *

# IT header view
class HeaderView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        site = siteList.objects.get(name='IT')
        site_serializer = SiteSerializer(site).data
        navbar = Navbar.objects.filter(site=site_serializer['id'],active=True)
        navbar_serializer = NavbarSerializer(navbar, many=True, context={'request':request}).data
        return Response({'navbar': navbar_serializer})

# Civil header view
class HeaderCivilView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        site = siteList.objects.get(name='Civil')
        site_serializer = SiteSerializer(site).data
        navbar = Navbar.objects.filter(site=site_serializer['id'],active=True)
        navbar_serializer = NavbarSerializer(navbar, many=True, context={'request':request}).data
        return Response({'navbar': navbar_serializer})

# total header
class HeaderBrandLogoViewAll(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        if DonateBrandLogo.objects.filter(active=True).first():
            Donatesite = DonateBrandLogo.objects.filter(active=True).first()
            Donatesite_serializer = DonateBrandLogoSerializer(Donatesite,many=False,context={'request':request}).data
        else:
            Donatesite_serializer = ''
        if ITBrandLogo.objects.filter(active=True).first():
            ITsite = ITBrandLogo.objects.filter(active=True).first()
            ITsite_serializer = ITBrandLogoSerializer(ITsite,many=False,context={'request':request}).data
        else:
            ITsite_serializer = ''
        if CivilBrandLogo.objects.filter(active=True).first():
            Civilsite = CivilBrandLogo.objects.filter(active=True).first()
            Civilsite_serializer = CivilBrandLogoSerializer(Civilsite,many=False,context={'request':request}).data
        else:
            Civilsite_serializer = ''

        data = {
            'Donatesite': Donatesite_serializer,
            'ITsite': ITsite_serializer,
            'Civilsite': Civilsite_serializer
        }
        return Response(data)
