from django.shortcuts import render
from rest_framework import generics, status
from Authentication.models import *
from Authentication.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import *
from .serializers import *
# Create your views here.
class UserDataGet(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

class EducationalQualificationView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EducationalQualification.objects.all()
    serializer_class = EducationalQualificationSerializer
    
    
    def post(self, request):
        try:
            instance = EducationalQualification.objects.get(user=request.user)    
        except EducationalQualification.DoesNotExist:
            serializer = EducationalQualificationSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
            return Response({"type":"success","msg":"Education Data Successfully Updated "})
        
        serializer = EducationalQualificationSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type":"success","msg":"Education Data Successfully Updated "})
        return Response({"type":"error","msg": serializer.errors, "status":status.HTTP_400_BAD_REQUEST})

class SocialMediaLinkView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SocialMediaLink.objects.all()
    serializer_class = SocialMediaLinkSerializer
    
    def post(self, request):
        try:
            instance = SocialMediaLink.objects.get(user=request.user)    
        except SocialMediaLink.DoesNotExist:
            serializer = SocialMediaLinkSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
            return Response({"type":"success","msg":"Social Link Successfully Updated "})
        
        serializer = SocialMediaLinkSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type":"success","msg":"Social Link Successfully Updated "})
        return Response({"type":"error","msg": serializer.errors, "status":status.HTTP_400_BAD_REQUEST})

class CompanyDetailView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = CompanyDetail.objects.all()
    serializer_class = CompanyDetailSerializer
    
    def post(self, request):
        try:
            instance = CompanyDetail.objects.get(user=request.user)    
        except CompanyDetail.DoesNotExist:
            serializer = CompanyDetailSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
            return Response({"type":"success","msg":"Company Data Successfully Updated "})
        
        serializer = CompanyDetailSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type":"success","msg":"Company Data Successfully Updated "})
        return Response({"type":"error","msg": serializer.errors, "status":status.HTTP_400_BAD_REQUEST})

class PresentAddressView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PresentAddress.objects.all()
    serializer_class = PresentAddressSerializer
    
    def post(self, request):
        try:
            instance = PresentAddress.objects.get(user=request.user)    
        except PresentAddress.DoesNotExist:
            serializer = PresentAddressSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
            return Response({"type":"success","msg":"Present Address Successfully Updated "})
        
        serializer = PresentAddressSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type":"success","msg":"Present Address Successfully Updated "})
        return Response({"type":"error","msg": serializer.errors, "status":status.HTTP_400_BAD_REQUEST})


class PermanentAddressView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PermanentAddress.objects.all()
    serializer_class = PermanentAddressSerializer
    
    def post(self, request):
        try:
            instance = PermanentAddress.objects.get(user=request.user)    
        except PermanentAddress.DoesNotExist:
            serializer = PermanentAddressSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
            return Response({"type":"success","msg":"Permanent Address Successfully Updated "})
        
        serializer = PermanentAddressSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type":"success","msg":"Permanent Address Successfully Updated "})
        return Response({"type":"error","msg": serializer.errors, "status":status.HTTP_400_BAD_REQUEST}) 

class Contact_infoView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Contact_info.objects.all()
    serializer_class = Contact_infoSerializer
    
    def post(self, request):
        try:
            instance = Contact_info.objects.get(user=request.user)    
        except Contact_info.DoesNotExist:
            serializer = Contact_infoSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
            return Response({"type":"success","msg":"Contact Info Successfully Updated "})
        
        serializer = Contact_infoSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type":"success","msg":"Contact Info Successfully Updated "})
        return Response({"type":"error","msg": serializer.errors, "status":status.HTTP_400_BAD_REQUEST}) 


class userDataUpdate(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    http_method_names = ['patch']
    queryset = User.objects.all()
    serializer_class = UserProfileUpdateSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response({"type":"success","msg": "Profile successfully updated"})

        else:
            return Response({"type": "error", "msg": "Update failed"})

