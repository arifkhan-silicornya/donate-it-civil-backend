from .serializers import *
from .header_serializers import *
from .footer_serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.pagination import PageNumberPagination
from Civil.models import *
from Civil.OrderModel import *
from Civil.OrderSerializer import CreateOrderCivilSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import (ListModelMixin, CreateModelMixin,  UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin)

class UpdateOrder(APIView):
    permission_classes = (IsAdminUser,)

    def patch(self, request, pk):
        try:
            instance = OrderCivil.objects.get(id=pk)    
        except OrderCivil.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CreateOrderCivilSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(status='pay')
            return Response({"type": "success", "msg": "Order successfully updated"})
        return Response({"type": "error", "msg": "Order updation failed"})

class CancelOrder(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk):
        try:
            print(pk)
            if OrderCivil.objects.filter(id=pk).exists():
                OrderCivil.objects.filter(id=pk).update(status='can')
                return Response({"type": "success", "msg": "Order Canceled successfully"})
            else:
                return Response({"type": "error", "msg": "Order not exist"})
        except OrderCivil.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

class WorkingOrder(APIView):
    permission_classes = [IsAdminUser]

    def patch(self,  request, pk):
        try:
            if OrderCivil.objects.filter(id=pk).exists():
                OrderCivil.objects.filter(id=pk).update(status='wor')
                return Response({"type": "success", "msg": "Order Working Now"})
            else:
                return Response({"type": "error", "msg": "Order not exist"})
        except OrderCivil.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

class CompleteOrder(APIView):
    permission_classes = [IsAdminUser]

    def patch(self,  request, pk):
        try:
            if OrderCivil.objects.filter(id=pk).exists():
                OrderCivil.objects.filter(id=pk).update(status='com')
                return Response({"type": "success", "msg": "Order Completed"})
            else:
                return Response({"type": "error", "msg": "Order not exist"})
        except OrderCivil.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

class DeliveredOrder(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = DeliveryFileCivil.objects.all()
    serializer_class = DeliveryFileSerializer
    def post(self,  request, pk):
        try:
            if OrderCivil.objects.filter(id=pk).exists():
                OrderCiv= OrderCivil.objects.get(id=pk)
                serializer = self.get_serializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save(ordercivil=OrderCiv)
                    OrderCivil.objects.filter(id=pk).update(status='del')
                    return Response({"type": "success", "msg": "Order file Delivered"})
                else:
                    return Response({"type": "error", "msg": "failed to delivered!"})
            else:
                return Response({"type": "error", "msg": "Order not exist"})
        except OrderCivil.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
