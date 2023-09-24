from .serializers import *
from .header_serializers import *
from .footer_serializers import *
from rest_framework.views import *
from rest_framework.response import Response
from rest_framework.permissions import *
from IT.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,RetrieveAPIView,UpdateAPIView

class NavbarCreateView(ListCreateAPIView):
    queryset = Navbar.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = NavbarSerializer
    
    def create(self, request, *args, **kwargs):
        site_civil = siteList.objects.get(name='Civil')
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(site=site_civil)
            return Response({"type": "success", "msg": "Header section succesfully created"})
        return Response({"type": "error", "msg": "Header section creation failed"})
    def get(self, request):
        site_civil = siteList.objects.get(name='Civil')
        queryset = Navbar.objects.filter(site=site_civil)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class NavbarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Navbar.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = NavbarSerializer
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        site_civil = siteList.objects.get(name='Civil')
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(site=site_civil)
            return Response({"type": "success", "msg": "Header section succesfully updated"})
        return Response({"type": "error", "msg": "Header section updation failed"})


class ITBrandList(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = CivilBrandLogo.objects.all()
    serializer_class = CivilBrandLogoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Brand IT succesfully created"})
        return Response({"type": "error", "msg": "Brand IT creation failed"})

    def get(self,request):
        queryset = CivilBrandLogo.objects.all()
        return Response(self.serializer_class(queryset, many=True,context={'request':request}).data)

class ITBrandUpdateRetrieve(RetrieveAPIView,UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = CivilBrandLogo.objects.all()
    serializer_class = CivilBrandLogoSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(request.data)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Brand data succesfully updated"})
        return Response({"type": "error", "msg": "Brand data updation failed"})