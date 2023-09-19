from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .OrderView import *


urlpatterns = [

        path('view-all/', Civil_Page_ViewSet.as_view(), name='Civil_Home_view'),
        path('contact-msg-send/', Contact_ViewSet.as_view(), name='Civil_Home_view'),

        # order
        path('create-order/', CreateOrderViewCivil.as_view(), name='Create-it-order'),
        path('save-pdf-order-other/', OrderAndOtherPDFUpload.as_view(), name='order-other-pdf'),
        path('self-order-view-all/', ViewAllSelfOrder.as_view(), name='self-order-list-all'),


        # product
        path('product/', ProductViewIT.as_view(), name='Product'),
        path('product/<int:pk>/', ProductViewIT.as_view(), name='Product'),
        
        # service
        path('service-link/', ServicesLinkList.as_view(), name='service-link-list'),
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)