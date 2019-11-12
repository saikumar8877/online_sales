"""admin_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path
from django.views.generic import ListView

from adminapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainpage),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('merchant_register/',views.merchant_register,name='merchant_register'),
    path('merchnat_login/',views.merchnat_login,name='merchnat_login'),
    path('logout/',views.logoutAdmin,name='logout'),
    path('addmerchant/',views.addmerchant,name='addmerchant'),
    path('Home/',views.homepage,name='Home'),
    path('savemerchant/',views.savemerchant),
    path('view_merchants/',views.viewMerchants,name='view_merchants'),
    path('deletemerchant/',views.deletemerchant,name='deletemerchant'),
    path('deleting/',views.deletingMerchant,name='deleting'),
    path('checklogin/<str:email>&<str:pwd>/',views.CheckMechantLoginDetails.as_view()),
    path('changingpassword/<str:email>&<str:pwd>/',views.ChangingMerchantPassword.as_view()),
    path('saving_product_details/',views.SaveMerchantPdetails.as_view())
]
