from django.shortcuts import render
import random
from .models import *
from rest_framework import generics, status, filters
from rest_framework.views import *
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import *
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
import datetime
from django.contrib.auth.models import update_last_login
# Create your views here.

   
   


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        try:
            username = request.data["username"]
            email = request.data["email"]
            password  = request.data["password"]
            confirm_password  = request.data["confirm_password"]
            if password != confirm_password:
                return Response({"type":"error","msg":"Passwords do not match"})    
            if User.objects.filter(email=email).exists():
                return Response({"type":"error","msg":"User with email already exist"})    
            if User.objects.filter(username=username).exists():
                return Response({"type":"error","msg":"User with username already exist"})    
        except:
            return Response({"type":"error","msg":"Please send all data"})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()    

        serializer1 = EducationalQualificationSerializer(data=request.data,partial=True)
        serializer1.is_valid(raise_exception=True)
        serializer1.save(user=user)

        serializer3 = CompanyDetailSerializer(data=request.data,partial=True)
        serializer3.is_valid(raise_exception=True)
        serializer3.save(user=user)

        serializer4 = PresentAddressSerializer(data=request.data,partial=True)
        serializer4.is_valid(raise_exception=True)
        serializer4.save(user=user)

        serializer5 = PermanentAddressSerializer(data=request.data,partial=True)
        serializer5.is_valid(raise_exception=True)
        serializer5.save(user=user)

        serializer6 = Contact_infoSerializer(data=request.data,partial=True)
        serializer6.is_valid(raise_exception=True)
        serializer6.save(user=user)

        if CodeVerification.objects.filter(user=user).exists() :

            CodeVer = CodeVerification.objects.get(user=user)
            CodeVer.code = random.randint(100000,999999)
            CodeVer.createDate = x.strftime("%x %X")
            CodeVer.expiredDate = x2.strftime("%x %X")
            CodeVer.save()
        
        else:
            CodeVer = CodeVerification()
            CodeVer.user = user
            CodeVer.code = random.randint(100000,999999)

        # Perform email verification logic here

        mail_subject = 'Activate your account'
        message = render_to_string('registration/email_verification.html', {
            'user': user,
            'uid': user.pk,
            'token': CodeVer.code,
        })
        message = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, [user.email,])
        message.content_subtype = "html"
        
        if (message.send(fail_silently=False)) :
            CodeVer.save()
            return Response({'type':'success','msg': 'A verification mail sent to your account.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'type':'error','msg': 'Mail did not not sent to your account.'})
            



# User Acc verify after verification

class UserCodeVerifyView(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    queryset = CodeVerification.objects.all()
    serializer_class = CodeVerificationSerializer
    
    def post(self, request, *args, **kwargs):
        x = datetime.datetime.now()
        try:
            email=request.data["email"]
            code=request.data["code"]
        except:
            return Response({"type":"error","msg":"username or password not found."})
        
        user_obj = User.objects.filter(email=email).first() or User.objects.filter(username__icontains=email).first()

        if CodeVerification.objects.filter(user=user_obj,code=code).exists() :
            user = CodeVerification.objects.get(user=user_obj)
            print(user.createDate)
            print(user.expiredDate)
            if(user.createDate > user.expiredDate ) :
                return Response({'type':'error','msg': 'Code Expired. Generate New Code.'})
            else:
                user_obj.is_verified =True
                user_obj.is_active =True
                user_obj.save()
                return Response({'type':'success','msg': 'Your Account is verified. You can login now.'})
        else:
            return Response({'type':'error','msg': 'Verification not successfull. User or Code not valid.'})


# Custom login view 
class CustomUserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
        except:
            return Response({"type":"eror","msg":"Email or Username, and Password not send with request"})

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
        elif User.objects.filter(email=username).exists():
            user = User.objects.get(email=username)
        else:
            return Response({"type":"error","msg":"User not found"})
        
        if user.is_active == False:
            return Response({"type":"error","msg":"User not active"})
        
        if user.is_verified == False:
            return Response({"type":"error","msg":"User not verified"})
        

        if user.check_password(password) and user.is_active and user.is_verified: 
            serializer = UserLoginSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.validated_data['username']
                password = serializer.validated_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    refresh = RefreshToken.for_user(user)
                    update_last_login(None, user)
                    AdminData = UserSerializer(user,many=False)
                    return Response({'refresh': str(refresh), 'access': str(refresh.access_token),"user":AdminData.data})
                else:
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"type":"error","msg":"Wrong Password ! try again"})


# Generate New verification Code

class GenerateUserCode(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    queryset = CodeVerification.objects.all()
    serializer_class = GenerateCodeSerializer
    
    def post(self, request, *args, **kwargs):
        x = datetime.datetime.now()
        x2 = datetime.datetime.now() + datetime.timedelta(minutes=120)
        try:
            email=request.data["email"]
        except:
            return Response({"type":"error","msg":"email not found."})
        
        user_obj = User.objects.filter(email=email).first() or User.objects.filter(username__icontains=email).first()

        if CodeVerification.objects.filter(user=user_obj).exists() :
            user = CodeVerification.objects.get(user=user_obj)
            currentDT = x.strftime("%x %X") 
            expireDT = x2.strftime("%x %X") 
            newCode = random.randint(100000,999999)

            user.code = newCode
            user.createDate = currentDT
            user.expiredDate = expireDT
            
            mail_subject = 'Activate your account'
            message = render_to_string('registration/email_verification.html', {
                'user': user_obj,
                'uid': user_obj.pk,
                'token': newCode,
            })
            message = EmailMessage(mail_subject, message, settings.EMAIL_HOST_USER, [user_obj.email,])
            message.content_subtype = "html"
            
            if (message.send(fail_silently=False)) :
                user.save()
                return Response({'type':'success','msg': 'A verification mail sent to your account.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'type':'error','msg': 'Mail did not not sent to your account.'})
        else:
            return Response({'type':'error','msg': 'User not valid.'})


class ResetPasswordView(generics.RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user 
            serializer.update(user, serializer.validated_data)
            return Response({'type':'success',"message": "Password reset successful."}, status=status.HTTP_200_OK)
        else:
            return Response({'type':'error','msg':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# user can change password when login
class ChangePasswordView(generics.RetrieveUpdateAPIView):
    
    serializer_class = ChangePasswordSerializer
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user  # Assuming the user is authenticated
            serializer.update(user, serializer.validated_data)
            return Response({'type':'success',"msg": "Password Changed successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({'type':'error','msg':"Fill carefully before submit","status":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class UsernameExist(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']

class UserDataGet(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    
