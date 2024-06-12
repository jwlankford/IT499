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
    path('small_order', views.small_order, name='small_order'),
    path('med_order', views.med_order, name='med_order'),
    path('ent_order', views.ent_order, name='ent_order'),
    path('thankyou', views.thankyou, name='thankyou'),
]