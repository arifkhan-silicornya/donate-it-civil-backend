from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from IT.Paymentserializers import *
from IT.Payment_Model import *
from IT.OrderModel import OrderIt
from rest_framework.decorators import api_view, permission_classes

@api_view(('GET',))
@permission_classes([IsAuthenticated])
def get_dashboard_data(request):
    if request.method == 'GET':
        try:
            totalOrder = OrderIt.objects.filter().count()
            penOrder = OrderIt.objects.filter(status='pen').count()
            payOrder = OrderIt.objects.filter(status='pay').count()
            canOrder = OrderIt.objects.filter(status='can').count()
            worOrder = OrderIt.objects.filter(status='wor').count()
            comOrder = OrderIt.objects.filter(status='com').count()
            delOrder = OrderIt.objects.filter(status='del').count()
            totalTransaction = TransactionModel.objects.filter().count()

            
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