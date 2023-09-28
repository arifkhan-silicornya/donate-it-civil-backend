from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from Civil.Paymentserializers import *
from Civil.Payment_Model import *
from Civil.OrderModel import OrderCivil
from rest_framework.decorators import api_view, permission_classes

@api_view(('GET',))
@permission_classes([IsAuthenticated])
def get_dashboard_data(request):
    if request.method == 'GET':
        try:
            totalOrder = OrderCivil.objects.filter().count()
            penOrder = OrderCivil.objects.filter(status='pen').count()
            payOrder = OrderCivil.objects.filter(status='pay').count()
            canOrder = OrderCivil.objects.filter(status='can').count()
            worOrder = OrderCivil.objects.filter(status='wor').count()
            comOrder = OrderCivil.objects.filter(status='com').count()
            delOrder = OrderCivil.objects.filter(status='del').count()
            totalTransaction = TransactionModelCivil.objects.filter().count()

            
            return Response({
                "allOrder":totalOrder,
                "penOrder":penOrder,
                "payOrder":payOrder,
                "canOrder":canOrder,
                "worOrder":worOrder,
                "comOrder":comOrder,
                "delOrder":delOrder,
                "TotalTransaction":totalTransaction,
                })
        except:
            return Response({"type":"error","msg":"Login required"})
    else:
        return Response({"type":"error","msg":"Wrong method"})