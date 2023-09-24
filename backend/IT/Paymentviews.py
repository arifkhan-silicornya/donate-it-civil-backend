from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from .Paymentserializers import *
from .Payment_Model import *
from .OrderModel import OrderIt

# Create your views here.
class CompanyAccount_View(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CompanyAccount.objects.filter(active=True).all()
    serializer_class = CompanyAccount_Serializer

class Payment_Method_View(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PaymentMethod.objects.filter(active=True).all()
    serializer_class = PaymentMethodSerializer


class CreateTransaction(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionModel_Serializer

    def post(self, request):
        try:
            order = request.data['order']
            bank = request.data['bank']
            if order == '' or bank == '':
                return Response({'type':'error','msg': 'order or bank is empty'})
            else:
                if CompanyAccount.objects.filter(id=bank).exists() and OrderIt.objects.filter(id=order).exists():
                    bankObj = CompanyAccount.objects.get(id=bank)
                    orderobj = OrderIt.objects.get(id=order)
                    serializer = self.get_serializer(data=request.data)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save(user=request.user, order = orderobj, bank = bankObj)
                        
                        SaveData =  serializer.data
                        total_online_pay = int(SaveData['amount']) + int(orderobj.total_online_paid)
                        if orderobj.payment_left > 0:
                            OrderIt.objects.filter(id=orderobj.id).update(total_online_paid = total_online_pay, payment_left= orderobj.payment_left-1)
                        else:
                            OrderIt.objects.filter(id=orderobj.id).update(total_online_paid = total_online_pay)

                        return Response({'type':'success','msg': 'Your Transaction Successfull'})
                    else:
                        return Response({'type':'error','msg': 'data not valid'})                        
                else:
                    return Response({'type':'error','msg': 'order or bank value not exist'})
        except:
            return Response({'type':'error','msg': 'order or bank not send with request'})
        
        
class GetTransaction(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TransactionModel.objects.all()
    serializer_class = TransactionModel_Serializer

    def get(self, request):
        isinstance =  TransactionModel.objects.filter(user = request.user).all().order_by('-id')
        return Response(self.serializer_class(instance = isinstance ,many=True ).data)