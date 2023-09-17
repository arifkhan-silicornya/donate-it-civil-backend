from .serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from .models import *

# Create your views here.
class CompanyAccount_View(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CompanyAccount.objects.filter(active=True).all()
    serializer_class = CompanyAccount_Serializer

class Payment_Method_View(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PaymentMethod.objects.filter(active=True).all()
    serializer_class = PaymentMethodSerializer

    