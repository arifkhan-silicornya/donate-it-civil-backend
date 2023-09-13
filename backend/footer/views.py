from django.shortcuts import render
from .serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *

# Create your views here.
class FooterViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = siteList.objects.filter(active=True)
    serializer_class = FooterSerializer



class NewsLetterViewSet(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = NewsLetter.objects.all()
    serializer_class = NewsLetterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'type':'success','msg': 'Thank You, Your Email is stored in our system.'})

    