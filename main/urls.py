from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path
urlpatterns=[

    path('',index, name='index'),
    path('all-customer/',all_customer, name='customers'),
    path('customer/<slug:slug>/',single_customer, name='customer'),
    path('account-statement/<slug:slug>/',account_statement, name='statement'),
    path('transfer-money/<slug:slug>/',transfer, name='transfer'),

            ]+ static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
