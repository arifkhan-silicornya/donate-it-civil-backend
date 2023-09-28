from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from .Paymentserializers import *
from .Payment_Model import *
from .OrderModel import OrderCivil
from rest_framework.decorators import api_view, permission_classes

@api_view(('GET',))
@permission_classes([AllowAny])
def get_dashboard_data(request):
    if request.method == 'GET':
        try:
            system_user = request.user
            totalOrder = OrderCivil.objects.filter(user=system_user).count()
            penOrder = OrderCivil.objects.filter(user=system_user,status='pen').count()
            payOrder = OrderCivil.objects.filter(user=system_user,status='pay').count()
            canOrder = OrderCivil.objects.filter(user=system_user,status='can').count()
            worOrder = OrderCivil.objects.filter(user=system_user,status='wor').count()
            comOrder = OrderCivil.objects.filter(user=system_user,status='com').count()
            delOrder = OrderCivil.objects.filter(user=system_user,status='del').count()
            totalTransaction = TransactionModelCivil.objects.filter(user=system_user).count()

            
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