from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

        # All data single user by id
        path('self/', UserDataGet.as_view(), name='user'),
        
        
        path('update-personal/', UserPersonalDataUpdate.as_view(), name='user-personal'),
        path('update-education/', EducationalQualificationView.as_view(), name='user-education'),
        path('update-company/', CompanyDetailView.as_view(), name='user-company'),
        path('update-present/', PresentAddressView.as_view(), name='user-present'),
        path('update-permanent/', PermanentAddressView.as_view(), name='user-permanent'),
        path('update-contact/', Contact_infoView.as_view(), name='user-contact'),
        path('profile-update/<int:pk>/', userDataUpdate.as_view(), name='profile-update'),
        path('profile-pic-update/', ProfilePictureUpdate.as_view(), name='profile-update'),

        
        
        path('social-link-create/', SocialLinkCreateByUser.as_view(), name='social-link-create'),
        path('social-link-delete/<int:pk>/', SocialMediaLinkDelete.as_view(), name='social-link-delete'),
        
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)