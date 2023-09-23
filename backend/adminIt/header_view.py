from .serializers import *
from .header_serializers import *
from .footer_serializers import *
from rest_framework.views import *
from rest_framework.response import Response
from rest_framework.permissions import *
from IT.models import *
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView,UpdateAPIView
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,  UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin)

class ITBrandList(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = ITBrandLogo.objects.all()
    serializer_class = ITBrandLogoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Brand IT succesfully created"})
        return Response({"type": "error", "msg": "Brand IT creation failed"})

    def get(self,request):
        queryset = ITBrandLogo.objects.all()
        return Response(self.serializer_class(queryset, many=True,context={'request':request}).data)

class ITBrandUpdateRetrieve(RetrieveAPIView,UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = ITBrandLogo.objects.all()
    serializer_class = ITBrandLogoSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type": "success", "msg": "Brand data succesfully updated"})
        return Response({"type": "error", "msg": "Brand data updation failed"})
