"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from application import views
from application import product_seller
from application import consumer
from application import Selling

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('salreg/',product_seller.product_salers),
    path('conreg/',consumer.consumer_reg),
    path('selview/',product_seller.pro_sal_view),
    path('update_sal/<id>/',product_seller.update_sal, name="updatesal"),
    path('deletesal/<id>/',product_seller.delete_sal, name="deletesal"),
    path('view/',consumer.view),
    path('update/<id>/',consumer.update, name="update"),
    path('delete/<id>/',consumer.delete, name="delete"),
    path('product/<email>/',Selling.postproduct, name="product"),
    path('pslogin/',Selling.log_in),
    # path('login/',Selling.login),
    path('pslogout/',Selling.log_out),
    path('myview/<email>/',Selling.my_products, name='myview'),
    path('updatepro/<id>/',Selling.pro_update, name='updatepro'),
    path('deletepro/<id>/',Selling.pro_delete, name='deletepro'),
    path('cuslogin/',consumer.con_login),
    path('cuslogout/<email>/',consumer.con_logout,name = 'cuslogout'),
    path('searchbar/<email>/',consumer.searchbar, name='search'),
    path('buy/<no>/<cemail>/',consumer.buying, name='purchase'),
    path('buyed/<no>/<cons>/<qty>/<amt>/', consumer.final, name = "final"),
    path('pview/<pno>/<cemail>/',consumer.pview, name = 'pview'),
    path('buyedproducts/<email>/',consumer.my_purchase, name= "buyedproducts"),
    path('contact/',views.contact),
    path('about/',consumer.about)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)