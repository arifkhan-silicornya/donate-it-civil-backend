from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
        # IT header
        path('header-view/', HeaderView.as_view(), name='header-view'),
        
        #  Civil header
        path('civil-header/', HeaderCivilView.as_view(), name='civil-header-view'),

        # all brand
        path('brands-logos/', HeaderBrandLogoViewAll.as_view(), name='brands-logos'),


   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)