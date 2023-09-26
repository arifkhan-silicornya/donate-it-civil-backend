from .serializers import *
from rest_framework.views import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .AdminSerializer import *
from django.contrib.auth.models import update_last_login

class AdminLoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']
        except:
            return Response({"type":"eror","msg":"Email or Username, and Password not send with request"})

        if User.objects.filter(email=username,is_superuser=True).exists():
            user = User.objects.get(email=username)
        else:
            return Response({"type":"error","msg":"Admin user not found"})

        if user.check_password(password):
            serializer = AdminLoginSerializer(data=request.data)
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