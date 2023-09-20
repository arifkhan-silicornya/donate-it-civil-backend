from .serializers import *
from .header_serializers import *
from .footer_serializers import *
from rest_framework.views import *
from rest_framework.response import Response
from rest_framework.permissions import *
from IT.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class footerSectionListCreateView(ListCreateAPIView):
    queryset = footerSection.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerSectionSerializer
    
    def create(self, request, *args, **kwargs):
        if siteList.objects.filter(name='Civil').exists():
            site_civil = siteList.objects.get(name='Civil')
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(site=site_civil)
            return Response({"type": "success", "msg": "Footer section succesfully created"})
        return Response({"type": "error", "msg": "Footer section creation failed"})
    def get(self, request):
        if siteList.objects.filter(name='Civil').exists():
            site_civil = siteList.objects.get(name='Civil')
        allData =  footerSection.objects.filter(site =site_civil).all()
        serializer = self.get_serializer(allData, many=True).data
        return Response(serializer)
    
class footerSectionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerSection.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerSectionSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if siteList.objects.filter(name='Civil').exists():
            site_civil = siteList.objects.get(name='Civil')
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(site=site_civil)
            return Response({"type": "success", "msg": "Footer section succesfully updated"})
        return Response({"type": "error", "msg": "Footer section updation failed"})

        
    
    
    
class footerItemListCreateView(ListCreateAPIView):
    queryset = footerItem.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerItemSerializer
    
    def create(self, request, *args, **kwargs):
        section = request.data['footerSection']
        if footerSection.objects.filter(title=section).exists():
            footer_section = footerSection.objects.get(title=section).first()
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(footerSection=footer_section)
            return Response({"type": "success", "msg": "Footer item succesfully created"})
        return Response({"type": "error", "msg": "Footer item creation failed"})
    def get(self, request):
        if siteList.objects.filter(name='Civil').exists():
            site_civil = siteList.objects.get(name='Civil')
        if footerSection.objects.filter(site =site_civil).exists():
            allData =  footerSection.objects.filter(site =site_civil).all()
        serializer = footerSectionSerializer(allData, many=True).data
        print(serializer)
        data = []
        for section in serializer:
            print(section)
            item = footerItem.objects.filter(footerSection=section['id'])
            item_serializer = footerItemSerializer(item, many=True).data
            data.append(item_serializer)
        return Response({"data":data})
    

class footerItemRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerItem.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerItemSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        f_section = request.data['footerSection']
        if footerSection.objects.filter(title=f_section).exists():
            footer_section = footerSection.objects.filter(title=f_section).first()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(footerSection=footer_section)
            return Response({"type": "success", "msg": "Footer item successfully updated"})
        return Response({"type": "error", "msg": "Footer item updation failed"})
    
    
class footerHeadOfficeListCreateView(ListCreateAPIView):
    queryset = footerHeadOffice.objects.all()
    permission_classes = [AllowAny]
    serializer_class = footerHeadOfficeSerializer
    
    def create(self, request, *args, **kwargs):
        if siteList.objects.filter(name='Civil').exists():
            site_civil = siteList.objects.get(name='Civil')
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(siteList=site_civil)
            return Response({"type": "success", "msg": "Head office succesfully created"})
        return Response({"type": "error", "msg": "Head office  creation failed"})
    def get(self, request):
        if siteList.objects.filter(name='Civil').exists():
            site_civil = siteList.objects.get(name='Civil')
        allData =  footerHeadOffice.objects.filter(siteList =site_civil).all()
        serializer = self.get_serializer(allData, many=True).data
        return Response(serializer)
    
class footerHeadOfficeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerHeadOffice.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerHeadOfficeSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        site_civil = siteList.objects.get(name='Civil')
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(siteList=site_civil)
            return Response({"type": "success", "msg": "Head office succesfully updated"})
        return Response({"type": "error", "msg": "Head office updation failed"})

    

class footerSocialIconListCreateView(ListCreateAPIView):
    queryset = footerSocialIcon.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerSocialIconSerializer
    def create(self, request, *args, **kwargs):
        if siteList.objects.filter(name='Civil').exists():
            site_civil = siteList.objects.get(name='Civil')
        serializer = self.get_serializer(data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save(siteList = site_civil)
            return Response({"type": "success", "msg": "Social icon succesfully created"})
        return Response({"type": "error", "msg": "Social icon creation failed"}) 
    def get(self, request):
        if siteList.objects.filter(name='Civil').exists():
            site_civil = siteList.objects.get(name='Civil')
        allData =  footerSocialIcon.objects.filter(siteList =site_civil).all()
        serializer = self.get_serializer(allData, many=True).data
        return Response(serializer)
       
class footerSocialIconRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = footerSocialIcon.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = footerSocialIconSerializer
    lookup_field = 'pk'
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data, partial=True)       
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Social icon successfully updated"})
        return Response({"type": "error", "msg": "Social icon updation failed"})
    
    
class NewsLetterListCreateView(ListCreateAPIView):
    queryset = NewsLetter.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = NewsLetterSerializer
    
class NewsLetterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = NewsLetter.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = NewsLetterSerializer