from django import views
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('contact-ape-30-technologies', views.ContactUs, name='contact-ape-30-technologies'),
    path('hire-ape-30-technologies', views.HireUs, name='hire-ape-30-technologies'),
    path('mobile-apps-built-by-ape-30-technologies', views.MobileApps, name='mobile-apps-built-by-ape-30-technologies'),
    
]
