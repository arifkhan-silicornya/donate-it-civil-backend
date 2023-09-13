from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [

        path('view-all/', HeaderSerializerViewSet.as_view(), name='footer_view'),

   ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)