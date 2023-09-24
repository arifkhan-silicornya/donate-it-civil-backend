from django.shortcuts import render
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination


from CivilAdmin.Paymentserializers import *
from Civil.Payment_Model import *



# =======================         PaymentMethod CRUD With APIView        ========================
class PaymentMethodAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get_data_pk(self, pk):
            return PaymentMethod.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = PaymentMethodSerializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = PaymentMethod.objects.all().order_by('-id')
            serializer = PaymentMethodSerializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk):
        instance = self.get_data_pk(pk)
        serializer = PaymentMethodSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated PaymentMethod"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "PaymentMethod Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "PaymentMethod Successfully activated"}, status=status.HTTP_200_OK)                           



# =======================         CompanyAccount CRUD With APIView        ========================
class CompanyAccountAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get_data_pk(self, pk):
            return CompanyAccount.objects.get(id=pk)
        
    def get(self, request, pk=None):
        if pk:
            instance = self.get_data_pk(pk)
            serializer = CompanyAccount_Serializer(instance, context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            instance = CompanyAccount.objects.all().order_by('-id')
            serializer = CompanyAccount_Serializer(instance, many=True, context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        try:
            payment_method_id = request.data['payment_method']
        except:    
            return Response({"type":"error","msg":"PaymentMethod Id not sent with request"})

        if PaymentMethod.objects.filter(id=payment_method_id).exists():
            payment_method = PaymentMethod.objects.get(id=payment_method_id)
        else:
            return Response({"type":"error","msg":"PaymentMethod not found"}) 

        serializer = CompanyAccount_Serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(payment_method=payment_method)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            payment_method_id = request.data['payment_method']
        except:    
            return Response({"type":"error","msg":"PaymentMethod Id not sent with request"})

        if PaymentMethod.objects.filter(id=payment_method_id).exists():
            payment_method = PaymentMethod.objects.get(id=payment_method_id)
        else:
            return Response({"type":"error","msg":"PaymentMethod not found"}) 
        instance = self.get_data_pk(pk)
        serializer = CompanyAccount_Serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(payment_method=payment_method)
            return Response({"status": status.HTTP_200_OK, "type": "success", "message": "Successfully updated CompanyAccount", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        instance = self.get_data_pk(pk)
        if instance.active == True:
            instance.active = False
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "CompanyAccount Successfully deactivated"}, status=status.HTTP_200_OK)        
        if instance.active == False:
            instance.active = True
            instance.save()
            return Response({"status": status.HTTP_200_OK,"type": "success", "message": "CompanyAccount Successfully activated"}, status=status.HTTP_200_OK)                           
