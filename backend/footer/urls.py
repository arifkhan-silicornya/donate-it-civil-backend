from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from .views import FooterItem_IT_View


urlpatterns = [

        # path('view-all/', FooterViewSet.as_view(), name='footer_view'),
        path('news-letter/', NewsLetterViewSet.as_view(), name='email_send'),
        
        # IT footer view
        path('footerview/', FooterView.as_view(), name='email_send'),
        
        # Civil footer view
        path('civil-footer/', FooterCivilView.as_view(), name='civil-footer'),

        # IT
        path('footer-items/', FooterItem_IT_View.as_view(), name='footer-items'),
        
        # civil
        path('civil-footer-items/', FooterItem_Civil_View.as_view(), name='footer-items'),
        
   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)