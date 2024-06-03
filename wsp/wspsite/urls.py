from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('pricing', views.pricing, name='pricing'),
    path('productinfo', views.productinfo, name='productinfo'),
    path('faqs', views.faqs, name='faqs'),
    path('about', views.about, name='about'),
    path('order', views.order, name='order'),
]