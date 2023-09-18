from .serializers import *
from .header_serializers import *
from .footer_serializers import *
from rest_framework.views import *
from rest_framework.response import Response
from rest_framework.permissions import *
from IT.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class NavbarCreateView(ListCreateAPIView):
    site_civil = siteList.objects.get(name='Civil')
    queryset = Navbar.objects.filter(site=site_civil)
    permission_classes = [IsAdminUser]
    serializer_class = NavbarSerializer
    
    def create(self, request, *args, **kwargs):
        site_civil = siteList.objects.get(name='Civil')
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(site=site_civil)
            return Response({"type": "success", "msg": "Header section succesfully created"})
        return Response({"type": "error", "msg": "Header section creation failed"})

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