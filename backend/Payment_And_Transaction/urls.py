from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [

    path('account-view-all/', CompanyAccount_View.as_view() ),
    path('methods-view-all/', Payment_Method_View.as_view() ),
        
   ]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)