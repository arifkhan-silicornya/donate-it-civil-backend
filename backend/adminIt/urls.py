from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
        path('banner-it/', BannerView.as_view(), name='Banner_it'),
        path('banner-it/<int:pk>/', BannerView.as_view(), name='Banner_it'),
        path('technologies-category/', TechnologiesCategoryView.as_view(), name='Technologies-category'),
        path('technologies-category/<int:pk>/', TechnologiesCategoryView.as_view(), name='Technologies-category'),
        path('technology/', TechnologyView.as_view(), name='Technology'),
        path('technology/<int:pk>/', TechnologyView.as_view(), name='Technology'),
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
        path('home/', HomeView.as_view(), name='Home'),
        path('home/<int:pk>/', HomeView.as_view(), name='Home'),
        path('category/', CategoryView.as_view(), name='Category'),
        path('category/<int:pk>/', CategoryView.as_view(), name='Category'),
        path('product/', ProductView.as_view(), name='Product'),
        path('product/<int:pk>/', ProductView.as_view(), name='Product'),
        path('order-it/', OrderITView.as_view(), name='OrderIt'),
        path('order-it/<int:pk>/', OrderITView.as_view(), name='OrderIt'),
        path('order-pdf/', OrderPdfView.as_view(), name='OrderPdf'),
        path('order-pdf/<int:pk>/', OrderPdfView.as_view(), name='OrderPdf'),
        
        path('other-pdf/', OtherPdfListCreateView.as_view(), name='OtherPdfListCreateView'),
        path('other-pdf/<int:pk>/', OtherPdfRetrieveUpdateDeleteView.as_view(), name='OtherPdfRetrieveUpdateDeleteView'),
        
        path('personal-info/', PersonalInfoListCreateView.as_view(), name='PersonalInfoListCreateView'),
        path('personal-info/<int:pk>/', PersonalInfoRetrieveUpdateDestroyView.as_view(), name='PersonalInfoRetrieveUpdateDestroyView'),
        
        path('present-address/', PresentAddressListCreateView.as_view(), name='PresentAddressListCreateView'),
        path('present-address/<int:pk>/', PresentAddressRetrieveUpdateDestroyView.as_view(), name='PresentAddressRetrieveUpdateDestroyView'),
        
        path('permanent-address/', PermanentAddressListCreateView.as_view(), name='PermanentAddressListCreateView'),
        path('permanent-address/<int:pk>/', PermanentAddressRetrieveUpdateDestroyView.as_view(), name='PermanentAddressRetrieveUpdateDestroyView'),
        
        path('company-detail/', CompanyDetailListCreateView.as_view(), name='CompanyDetailListCreateView'),
        path('company-detail/<int:pk>/', CompanyDetailRetrieveUpdateDestroyView.as_view(), name='CompanyDetailRetrieveUpdateDestroyView'),
        
        path('contact-info/', Contact_infoListCreateView.as_view(), name='Contact_infoListCreateView'),
        path('contact-info/<int:pk>/', Contact_infoRetrieveUpdateDestroyView.as_view(), name='Contact_infoRetrieveUpdateDestroyView'),
        
        path('social-media/', SocialMediaLinkListCreateView.as_view(), name='Contact_infoRetrieveUSocialMediaLinkListCreateViewpdateDestroyView'),
        path('social-media/<int:pk>/', SocialMediaLinkRetrieveUpdateDestroyView.as_view(), name='SocialMediaLinkRetrieveUpdateDestroyView'),
        
        path('site/', siteListCreateView.as_view(), name='siteListCreateView'),
        path('site/<int:pk>/', siteRetrieveUpdateDestroyView.as_view(), name='siteRetrieveUpdateDestroyView'),
        
        path('navbar/', NavbarCreateView.as_view(), name='NavbarCreateView'),
        path('navbar/<int:pk>/', NavbarRetrieveUpdateDestroyView.as_view(), name='NavbarRetrieveUpdateDestroyView'),
        
        path('footer-section/', footerSectionListCreateView.as_view(), name='footerSectionListCreateView'),
        path('footer-section/<int:pk>/', footerSectionRetrieveUpdateDestroyView.as_view(), name='footerSectionRetrieveUpdateDestroyView'),
        
        path('footer-item/', footerItemListCreateView.as_view(), name='footerItemListCreateView'),
        path('footer-item/<int:pk>/', footerItemRetrieveUpdateDestroyView.as_view(), name='footerItemRetrieveUpdateDestroyView'),
        
        path('head-office/', footerHeadOfficeListCreateView.as_view(), name='footerHeadOfficeListCreateView'),
        path('head-office/<int:pk>/', footerHeadOfficeRetrieveUpdateDestroyView.as_view(), name='footerHeadOfficeRetrieveUpdateDestroyView'),
        
        path('social-icon/', footerSocialIconListCreateView.as_view(), name='footerSocialIconListCreateView'),
        path('social-icon/<int:pk>/', footerSocialIconRetrieveUpdateDestroyView.as_view(), name='footerSocialIconRetrieveUpdateDestroyView'),
        
        path('payment-icon/', PaymentIconListCreateView.as_view(), name='PaymentIconListCreateView'),
        path('site/<int:pk>/', PaymentIconRetrieveUpdateDestroyView.as_view(), name='PaymentIconRetrieveUpdateDestroyView'),
        
        path('news-letter/', NewsLetterListCreateView.as_view(), name='NewsLetterListCreateView'),
        path('news-letter/<int:pk>/', NewsLetterRetrieveUpdateDestroyView.as_view(), name='NewsLetterRetrieveUpdateDestroyView'),
        
        
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)