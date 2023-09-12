from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .OrderView import *


urlpatterns = [

        path('view-all/', Civil_Page_ViewSet.as_view(), name='Civil_Home_view'),
        path('contact-msg-send/', Contact_ViewSet.as_view(), name='Civil_Home_view'),

        # order
        path('create-order/', CreateOrderView.as_view(), name='Civil_Home_view'),
        
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)