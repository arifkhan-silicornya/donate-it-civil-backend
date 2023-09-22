from django.shortcuts import render
from .serializers import *
from Header.serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *

# Create your views here.
# class FooterViewSet(generics.ListAPIView):
#     permission_classes = (AllowAny,)
#     queryset = siteList.objects.filter(active=True)
#     serializer_class = FooterSerializer
    
class ItFooterView(APIView):
    def get(self, request, *args, **kwargs):
        data = []
        site = siteList.objects.get(title='IT')

class NewsLetterViewSet(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'type':'success','msg': 'Thank You, Your Email is stored in our system.'})

class FooterView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        site = siteList.objects.get(name='IT')
        site_serializer = SiteSerializer(site).data
        footer_sections = footerSection.objects.filter(site=site_serializer['id'],active=True)
        footer_section_serializer = FooterSectionSerializer(footer_sections, many=True).data
        footerSections = []
        for footer_section in footer_section_serializer:
            items = footerItem.objects.filter(footerSection=footer_section['id'],active=True)
            footer_section['items'] = FooterItemSerializer(items, many=True).data
            footerSections.append(footer_section)
        
        headOffice_objects = footerHeadOffice.objects.filter(siteList=site_serializer['id'], active=True)
        footer_head_office_serializer = FooterHeadOfficeSerializer(headOffice_objects, many=True).data
        
        footer_social_icon_objects = footerSocialIcon.objects.filter(siteList=site_serializer['id'], active=True)
        footer_social_icon_serializer = FooterSocialIconSerializer(footer_social_icon_objects, many=True, context={'request':request}).data
        
        footer_payment_icon_objects = PaymentIcon.objects.filter(active=True).all()
        footer_payment_icon_serializer = PaymentIconSerializer(footer_payment_icon_objects, many=True, context={'request':request}).data
        return Response({'footerSections':footerSections, 'footerHeadOffices':footer_head_office_serializer, 'footerSocialIcon':footer_social_icon_serializer, 'paymentIcon':footer_payment_icon_serializer})
    

class FooterItem_IT_View(generics.ListAPIView):
    permission_classes=[AllowAny]
    serializer_class = FooterItemSerializer
    queryset = footerItem.objects.all()

    def get_queryset(self):
        return self.queryset.filter(link__icontains='/it',active=True)
    

# def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True).data
#         data = []
#         for ctg in serializer:
#             product_objects= Product.objects.filter(category=ctg['id'])
#             ctg['products'] = ProductSerializer(product_objects, many=True, context={'request': request}).data
#             data.append(ctg)
#         return Response(data)


# ---------------------------Civil Footer --------------------------------


class FooterCivilView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        civil_site = siteList.objects.get(name='Civil')
        site_serializer = SiteSerializer(civil_site).data
        footer_sections = footerSection.objects.filter(site=site_serializer['id'])
        footer_section_serializer = FooterSectionSerializer(footer_sections, many=True).data
        footerSections = []
        for footer_section in footer_section_serializer:
            items = footerItem.objects.filter(footerSection=footer_section['id'])
            footer_section['items'] = FooterItemSerializer(items, many=True).data
            footerSections.append(footer_section)
        
        headOffice_objects = footerHeadOffice.objects.filter(siteList=site_serializer['id'], active=True)
        footer_head_office_serializer = FooterHeadOfficeSerializer(headOffice_objects, many=True).data
        
        footer_social_icon_objects = footerSocialIcon.objects.filter(siteList=site_serializer['id'])
        footer_social_icon_serializer = FooterSocialIconSerializer(footer_social_icon_objects, many=True, context={'request':request}).data
        
        footer_payment_icon_objects = PaymentIcon.objects.all()
        footer_payment_icon_serializer = PaymentIconSerializer(footer_payment_icon_objects, many=True, context={'request':request}).data
        return Response({'footerSections':footerSections, 'footerHeadOffices':footer_head_office_serializer, 'footerSocialIcon':footer_social_icon_serializer, 'paymentIcon':footer_payment_icon_serializer})
    


class FooterItem_Civil_View(generics.ListAPIView):
    permission_classes=[AllowAny]
    serializer_class = FooterItemSerializer
    queryset = footerItem.objects.all()

    def get_queryset(self):
        return self.queryset.filter(link__icontains='/civil',active=True)
