from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .OrderView import *
from .Paymentviews import *
from .Dashboard_View import *

urlpatterns = [

        path('view-all/', SecurityPage_SerializerViewSet.as_view(), name='IT_Home_view'),
        path('contact-msg-send/', Contact_ViewSet.as_view(), name='IT_Home_view'),

        # all-active-services/
        path('all-active-services/', ServicesLinkList.as_view(), name='IT_Serices'),

        # all-active-technologies/
        path('all-active-technology/', TechnologiesCategoryView.as_view(), name='technology-active-list'),
        
        # all-active-security
        path('all-active-security/', user_SecurityView.as_view(), name='technology-active-list'),
        
        # notice
        path('all-active-notice/', user_NoticeView.as_view(), name='technology-active-list'),

        # company
        path('all-active-company/', user_CompanyView.as_view(), name='technology-active-list'),


        # order
        path('create-order/', CreateOrderView.as_view(), name='Create-it-order'),
        path('save-pdf-order-other/', OrderAndOtherPDFUpload.as_view(), name='order-other-pdf'),
        path('self-order-view-all/', ViewAllSelfOrder.as_view(), name='self-order-list-all'),

        path('global-location-view-all/', Global_location_ViewSet.as_view(), name='global-location-data'),

        path('technology-link/', TechnologyLinkList.as_view(), name='technology-link-list'),
        path('service-link/', ServicesLinkList.as_view(), name='service-link-list'),    
        path('readmore-link/', ReadmoreSerializer_View.as_view(), name='readmore-link-list'),        
        
        path('product/', ProductViewIT.as_view(), name='Product'),
        path('product/<int:pk>/', ProductViewIT.as_view(), name='Product'),

        
        path('category/', ProCategoryViewIT.as_view(), name='Category'),
        path('category/<int:pk>/', ProCategoryViewIT.as_view(), name='Category'),


        path('account-view-all/', CompanyAccount_View.as_view(), name='view-bank-details'),

        #transaction
        path('make-payment/', CreateTransaction.as_view(), name='make-payment'),
        path('get-all-transaction/', GetTransaction.as_view(), name='get-payment'),
        

        # dashbaord
        path('get-dashboard/', get_dashboard_data, name='dashboard'),
        
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)