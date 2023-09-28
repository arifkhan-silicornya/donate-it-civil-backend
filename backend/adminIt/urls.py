from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from IT.views import *
from .header_view import *
from .OrderManageView import *
from .dashboard_view import *

urlpatterns = [
        path('banner/', BannerView.as_view(), name='Banner_it'),
        path('banner/<int:pk>/', BannerView.as_view(), name='Banner_it'),
        
        path('bottom-banner/', BottomBannerView.as_view(), name='bottom-banner'),
        path('bottom-banner/<int:pk>/', BottomBannerView.as_view(), name='bottom-banner'),
        
        path('technologies-category/', TechnologiesCategoryAPIView.as_view(), name='Technologies-category'),
        path('technologies-category/<int:pk>/', TechnologiesCategoryAPIView.as_view(), name='Technologies-category'),
        
        path('technology/', TechnologyView.as_view(), name='Technology'),
        path('technology/<int:pk>/', TechnologyView.as_view(), name='Technology'),
        path('technology-active-deactive/<int:pk>/', TechnologyStatusChange.as_view(), name='Product-status'),
        path('notice/', NoticeView.as_view(), name='Notice'),
        path('notice/<int:pk>/', NoticeView.as_view(), name='Notice'),
        path('security/', SecurityView.as_view(), name='Security'),
        path('security/<int:pk>/', SecurityView.as_view(), name='Security'),
        path('contact/', ContactView.as_view(), name='Contact'),
        path('contact/<int:pk>/', ContactView.as_view(), name='Contact'),
        path('company/<int:pk>/', CompanyView.as_view(), name='Company'),
        path('company/', CompanyView.as_view(), name='Company'),
        path('services/', OurServicesView.as_view(), name='Services'),
        path('services/<int:pk>/', OurServicesView.as_view(), name='Services'),
        path('readmore/', ReadmoreView.as_view(), name='Readmore'),
        path('readmore/<int:pk>/', ReadmoreView.as_view(), name='Readmore'),
        path('home-template/', HomeTemplateView.as_view(), name='home-template'),
        path('home-template/<int:pk>/', HomeTemplateView.as_view(), name='home-template'),
        path('product-category/', CategoryView.as_view(), name='Category'),
        path('product-category/<int:pk>/', CategoryView.as_view(), name='Category'),
        path('product/', ProductView.as_view(), name='Product'),
        path('product/<int:pk>/', ProductView.as_view(), name='Product'),
        path('product-active-deactive/<int:pk>/', ProductStatusChange.as_view(), name='Product-status'),
        path('order-it/', OrderITView.as_view(), name='OrderIt'),
        path('order-it/<int:pk>/', OrderITView.as_view(), name='OrderIt'),
        path('order-pdf/', OrderPdfView.as_view(), name='OrderPdf'),
        path('order-pdf/<int:pk>/', OrderPdfView.as_view(), name='OrderPdf'),
        
        path('other-pdf/', OtherPdfListCreateView.as_view(), name='OtherPdfListCreateView'),
        path('other-pdf/<int:pk>/', OtherPdfRetrieveUpdateDeleteView.as_view(), name='OtherPdfRetrieveUpdateDeleteView'),
        
        path('personal-info/', PersonalInfoListCreateView.as_view(), name='PersonalInfoListCreateView'),
        path('personal-info/<int:pk>/', PersonalInfoRetrieveUpdateDestroyView.as_view(), name='PersonalInfoRetrieveUpdateDestroyView'),
        
        path('payment-method/', PaymentMethodListCreateView.as_view(), name='PaymentMethodListCreateView'),
        path('payment-method/<int:pk>/', PaymentMethodRetrieveUpdateDestroyView.as_view(), name='PaymentMethodRetrieveUpdateDestroyView'),
                
        path('account/', CompanyAccountListCreateView.as_view(), name='CompanyAccountListCreateView'),
        path('account/<int:pk>/', CompanyAccountRetrieveUpdateDestroyView.as_view(), name='CompanyAccountRetrieveUpdateDestroyView'),
        path('account-active-disable/<int:pk>/', CompanyAccountActive_Disable.as_view(), name='CompanyAccountRetrieveUpdateDestroyView'),
        
        path('permanent-address/', PermanentAddressListCreateView.as_view(), name='PermanentAddressListCreateView'),
        path('permanent-address/<int:pk>/', PermanentAddressRetrieveUpdateDestroyView.as_view(), name='PermanentAddressRetrieveUpdateDestroyView'),
        
        path('company-detail/', CompanyDetailListCreateView.as_view(), name='CompanyDetailListCreateView'),
        path('company-detail/<int:pk>/', CompanyDetailRetrieveUpdateDestroyView.as_view(), name='CompanyDetailRetrieveUpdateDestroyView'),
        
        path('contact-info/', Contact_infoListCreateView.as_view(), name='Contact_infoListCreateView'),
        path('contact-info/<int:pk>/', Contact_infoRetrieveUpdateDestroyView.as_view(), name='Contact_infoRetrieveUpdateDestroyView'),
        
        path('social-media/', SocialMediaLinkListCreateView.as_view(), name='Contact_infoRetrieveUSocialMediaLinkListCreateViewpdateDestroyView'),
        path('social-media/<int:pk>/', SocialMediaLinkRetrieveUpdateDestroyView.as_view(), name='SocialMediaLinkRetrieveUpdateDestroyView'),
        
        path('user-social-media/', SocialMediaListCreateAPIView.as_view(), name='SocialMediaListCreateAPIView'),
        
        path('site/', siteListCreateView.as_view(), name='siteListCreateView'),
        path('site/<int:pk>/', siteRetrieveUpdateDestroyView.as_view(), name='siteRetrieveUpdateDestroyView'),
        
        path('header/', NavbarCreateView.as_view(), name='NavbarCreateView'),
        path('header/<int:pk>/', NavbarRetrieveUpdateDestroyView.as_view(), name='NavbarRetrieveUpdateDestroyView'),
        
        path('footer-section/', footerSectionListCreateView.as_view(), name='footerSectionListCreateView'),
        path('footer-section/<int:pk>/', footerSectionRetrieveUpdateDestroyView.as_view(), name='footerSectionRetrieveUpdateDestroyView'),
        
        path('footer-item/', footerItemListCreateView.as_view(), name='footerItemListCreateView'),
        path('footer-item/<int:pk>/', footerItemRetrieveUpdateDestroyView.as_view(), name='footerItemRetrieveUpdateDestroyView'),
        
        path('head-office/', footerHeadOfficeListCreateView.as_view(), name='footerHeadOfficeListCreateView'),
        path('head-office/<int:pk>/', footerHeadOfficeRetrieveUpdateDestroyView.as_view(), name='footerHeadOfficeRetrieveUpdateDestroyView'),
        
        path('social-icon/', footerSocialIconListCreateView.as_view(), name='footerSocialIconListCreateView'),
        path('social-icon/<int:pk>/', footerSocialIconRetrieveUpdateDestroyView.as_view(), name='footerSocialIconRetrieveUpdateDestroyView'),
        
        path('payment-icon/', PaymentIconListCreateView.as_view(), name='PaymentIconListCreateView'),
        path('payment-icon/<int:pk>/', PaymentIconRetrieveUpdateDestroyView.as_view(), name='PaymentIconRetrieveUpdateDestroyView'),
        
        path('news-letter/', NewsLetterListCreateView.as_view(), name='NewsLetterListCreateView'),
        path('news-letter/<int:pk>/', NewsLetterRetrieveUpdateDestroyView.as_view(), name='NewsLetterRetrieveUpdateDestroyView'),
        
        path('global-loc/', GlobalListCreateAPIView.as_view(), name='GlobalListCreateAPIView'),
        path('global-loc/<int:pk>/', GlobalRetrieveUpdateDestroyAPIView.as_view(), name='GlobalRetrieveUpdateDestroyAPIView'),

        path('user-list/', UserListAPIView.as_view(), name='UserListAPIView'),
        path('orders/', OrderListAPIView.as_view(), name='OrderListAPIView'),
        path('pending-orders/', PendingOrderListAPIView.as_view(), name='PendingOrderListAPIView'),
        path('payment-orders/', PaymentOrderListAPIView.as_view(), name='PaymentOrderListAPIView'),
        path('working-orders/', WorkingOrderListAPIView.as_view(), name='WorkingOrderListAPIView'),
        path('cancelled-orders/', CancelledOrderListAPIView.as_view(), name='CancelledOrderListAPIView'),
        path('delivery-orders/', DeliveryOrderListAPIView.as_view(), name='DeliveryOrderListAPIView'),
        path('complete-orders/', CompletedOrderListAPIView.as_view(), name='CompletedOrderListAPIView'),
        
        path('transaction/', TransactionListAPIView.as_view() ),
        
        # ORder update
        
        path('update-pending-order/<int:pk>/', UpdateOrder.as_view() ),
        path('cancel-pending-order/<int:pk>/', CancelOrder.as_view() ),
        path('working-order/<int:pk>/', WorkingOrder.as_view() ),
        path('complete-order/<int:pk>/', CompleteOrder.as_view() ),
        path('deliver-order/<int:pk>/', DeliveredOrder.as_view() ),
        
        
        # Brand Logo
        path('create-view-brand/', ITBrandList.as_view() ),
        path('view-update-brand/<int:pk>/', ITBrandUpdateRetrieve.as_view()),
        
        
        # dashboard
        path('get-dashboard/', get_dashboard_data),


        
        
        # path('category-product/', CategoryProductView.as_view(), name='CategoryProductView'),
        
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)