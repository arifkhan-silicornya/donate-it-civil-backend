from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [

        path('view-all/', FooterViewSet.as_view(), name='footer_view'),
        path('view-all/', NewsLetterViewSet.as_view(), name='email_send'),

   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)