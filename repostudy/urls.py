"""repostudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from product.views import SellProduct, AddStock
from number.views import Number20

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^product_sell/(?P<pk>\d+)', SellProduct.as_view(),name='sell-product'),
    url(r'^add_stock/(?P<pk>\d+)', AddStock.as_view(),name='add-product'),
    url(r'^number_validation/(?P<number>\d+)', Number20.as_view(),name='great-number-20'),
]
