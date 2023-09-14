from django.shortcuts import render
from rest_framework import generics, status
from Authentication.models import *
from Authentication.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework.decorators import APIView
from .serializers import *
# Create your views here.
class UserDataGet(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        try:
            if User.objects.filter(id= request.user.id).exists():
                user = User.objects.get(id= request.user.id)
                return Response(self.serializer_class(user,many=False).data)
            else:
                return Response({"type":"error","msg":"Valid user not found"})
        except:
            return Response({"type":"error","msg":"User not found"})

class UserPersonalDataUpdate(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request):
        try:
            instance = User.objects.get(id=request.user.id)    
        except instance.DoesNotExist:
            return Response({"type":"error","msg": "User not Exist", "status":status.HTTP_400_BAD_REQUEST})    
        
        serializer = self.serializer_class(instance,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type":"success","msg":"User Data Successfully Updated "})
        return Response({"type":"error","msg": serializer.errors, "status":status.HTTP_400_BAD_REQUEST})

class EducationalQualificationView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EducationalQualification.objects.all()
    serializer_class = EducationalQualificationSerializer
    
    
    def post(self, request):
        try:
            instance = EducationalQualification.objects.get(user=request.user)    
        except instance.DoesNotExist:
            serializer = EducationalQualificationSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
            return Response({"type":"success","msg":"Education Data Successfully Updated "})
        
        serializer = EducationalQualificationSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"type":"success","msg":"Education Data Successfully Updated "})
        return Response({"type":"error","msg": serializer.errors, "status":status.HTTP_400_BAD_REQUEST})

# New Media Link Created
class SocialLinkCreateByUser(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SocialMediaLink.objects.all()
    serializer_class = User_SocialMediaLinkSerializer
    
    def post(self, request):
        try:
            instance = User.objects.filter(id=request.user.id)    
        except User.DoesNotExist:
            # serializer = SocialMediaLinkSerializer(data=request.data, partial=True)
            # if serializer.is_valid():
            #     serializer.save(user=request.user)
            return Response({"type":"error","msg":"Valid User not found "})
        
        if instance:
            serializer = self.serializer_class(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({"type":"success","msg":"Social Link Successfully Created "})
            else:
                return Response({"type":"error","msg": serializer.errors})
        else:
            return Response({"type":"error","msg": "User not found"})
        

class SocialMediaLinkDelete(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = SocialMediaLink.objects.all()
    serializer_class = User_SocialMediaLinkSerializer
    lookup_field = 'pk'

    def post(self,request,pk):
        try:
            instance = User.objects.get(id=request.user.id)    
            linkID = SocialMediaLink.objects.get(id=pk)    
        except instance.DoesNotExist:
            return Response({"type":"error","msg":"Valid User not found "})
    
        if instance and linkID :
            SocialMediaLink.objects.filter(user=instance,id=linkID.id).update(active=False)
            return Response({"type":"success","msg":"Link deleted "})
        else:
            return Response({"type":"error","msg":"Sorry, try again! "})



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
    permission_classes = [IsAuthenticated,]
    http_method_names = ['patch']
    queryset = User.objects.all()
    serializer_class = UserProfileUpdateSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response({"type":"success","msg": "Profile successfully updated"})

        else:
            return Response({"type": "error", "msg": "Update failed"})



class ProfilePictureUpdate(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        try:
            usr= request.user
            if usr:
                serializer = UserProfile_Pic_UpdateSerializer(usr, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"type":"success","msg":"Picture Updated","New_image":serializer.data})
                else:
                    return Response({"type":"error","msg": serializer.errors})
            else:
                return Response({"type":"error","msg":"Registered User not found"})
        except:
            return Response({"type":"error","msg": "User not found" })
