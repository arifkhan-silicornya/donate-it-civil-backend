from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, TokenVerifyView )
from .AdminLoginView import *
from django.db.models import Q

urlpatterns = [

        path('register/', UserRegistrationView.as_view(), name='user_registration'),

        # During registration
        path('code-verify/', UserCodeVerifyView.as_view(), name='user_verifiy'),
        path('code-generate/', GenerateUserCode.as_view(), name='generate_verifiy_code'),

        # if User forget his passowrd
        path('forget-password/', GenerateUserCode.as_view(), name='forget_password'),
        path('reset-password/', ResetPasswordView.as_view(), name='email_verify'),
        
        # if user want to change his password
        path('change-password/', ChangePasswordView.as_view(), name='email_verify'),
        

        #login user 
        path('login/', CustomUserLoginView.as_view(), name='token_obtain_pair'),
        path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('verify/', TokenVerifyView.as_view(), name='token_verify'),

        #login user 
        path('admin-login/', AdminLoginAPIView.as_view(), name='admin_login'),

        # username check
        path('username/', UsernameExist.as_view(), name='user_search'),
        
        path('user/<int:id>/', UserDataGet.as_view(), name='user'),
        



        
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)