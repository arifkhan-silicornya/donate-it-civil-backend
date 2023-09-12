from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

        # All data single user by id
        path('<int:pk>/', UserDataGet.as_view(), name='user'),
        
        
        path('update-education/', EducationalQualificationView.as_view(), name='user-education'),
        path('update-social/', SocialMediaLinkView.as_view(), name='user-social'),
        path('update-company/', CompanyDetailView.as_view(), name='user-company'),
        path('update-present/', PresentAddressView.as_view(), name='user-present'),
        path('update-permanent/', PermanentAddressView.as_view(), name='user-permanent'),
        path('update-contact/', Contact_infoView.as_view(), name='user-contact'),
        path('profile-update/<int:pk>/', userDataUpdate.as_view(), name='profile-update'),

        
        
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)