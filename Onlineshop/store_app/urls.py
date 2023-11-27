"""
URL configuration for Onlineshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from store_app import views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cart', views.cart, name='cart'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('order_complete', views.order_complete, name='order_complete'),
    path('place_order', views.place_order, name='bplace_orderase'),
    path('product_detail/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('store/<slug:category_slug>/', views.store, name='store'),
    path('store/', views.store, name='store'),
    path('search_result', views.search_result, name='search_result'),
    path('home', views.home, name='home'),
    ]
