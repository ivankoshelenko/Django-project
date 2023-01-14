from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.urls import path
from.views import *


urlpatterns = [
    path('',demand)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)