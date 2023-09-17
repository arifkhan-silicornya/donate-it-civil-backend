from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .OrderView import *


urlpatterns = [
      path('create-site-list/', SiteListView.as_view(), name='create_site_list'),
      path('create-navbar/', CreateNavbarView.as_view(), name='create_navbar'),


      # BannerCivil apiview crud url
      path('banner-civil/', BannerCivilAPIView.as_view()),
      path('banner-civil/<int:pk>/', BannerCivilAPIView.as_view()),

      # FeatureWorksCategory apiview crud url
      path('feature-work-category/', FeatureWorksCategoryAPIView.as_view()),
      path('feature-work-category/<int:pk>/', FeatureWorksCategoryAPIView.as_view()),

      # FeatureWorks apiview crud url
      path('feature-work/', FeatureWorksAPIView.as_view()),
      path('feature-work/<int:pk>/', FeatureWorksAPIView.as_view()),

      # Architecture apiview crud url
      path('architecture/', ArchitectureAPIView.as_view()),
      path('architecture/<int:pk>/', ArchitectureAPIView.as_view()),

      # OurServices apiview crud url
      path('services/', OurServicesAPIView.as_view()),
      path('services/<int:pk>/', OurServicesAPIView.as_view()),

      # Readmore apiview crud url
      path('read-more/', ReadmoreAPIView.as_view()),
      path('read-more/<int:pk>/', ReadmoreAPIView.as_view()),

      # SecurityPageAPIView crud url
      path('security/', SecurityPageAPIView.as_view()),
      path('security/<int:pk>/', SecurityPageAPIView.as_view()),

      # ContactPageAPIView crud url
      path('contact/', ContactPageAPIView.as_view()),
      path('contact/<int:pk>/', ContactPageAPIView.as_view()),

      # ProductCategoryModelAPIView crud url
      path('product-category/', ProductCategoryModelAPIView.as_view()),
      path('product-category/<int:pk>/', ProductCategoryModelAPIView.as_view()),

      # ProductModelAPIView crud url
      path('product/', ProductModelAPIView.as_view()),
      path('product/<int:pk>/', ProductModelAPIView.as_view()),

      # NoticeModelAPIView crud url
      path('notice/', NoticeModelAPIView.as_view()),
      path('notice/<int:pk>/', NoticeModelAPIView.as_view()),

      # CompanyModelAPIView crud url
      path('company/', CompanyModelAPIView.as_view()),
      path('company/<int:pk>/', CompanyModelAPIView.as_view()),

      # BottomBannerAPIView crud url
      path('bottom-banner/', BottomBannerAPIView.as_view()),
      path('bottom-banner/<int:pk>/', BottomBannerAPIView.as_view()),

      # GlobalLocationAPIView crud url
      path('global-location/', GlobalLocationAPIView.as_view()),
      path('global-location/<int:pk>/', GlobalLocationAPIView.as_view()),

      # CreateOrderView url
      path('create-order/', CreateOrderView.as_view()),
      path('order-view-all/', Order_ViewSet.as_view()),
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)