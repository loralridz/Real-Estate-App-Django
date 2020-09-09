
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('property/',PropertyListView.as_view(), name="property"),
    path('about/',about, name="about"),
    path('blog/',blog, name="blog"),
    path('contact/',contact, name="contact"),
    path('property/<int:propertyid>',propertysingle, name="propertysingle"),
    path('searchproperty/',searchproperty, name="searchproperty")
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

