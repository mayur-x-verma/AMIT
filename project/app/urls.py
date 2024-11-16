from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = "home"),
    path('service', views.service_page, name = "service"),
    path('about', views.about_page, name = "about"),
    # path('products/', views.product_page, name = "products"),
    path('career', views.career, name = "career"),
    # path('career', views.career_view, name = "career"),
    path('clients', views.clients, name='clients'), 
    path('contact',views.contact, name = "contact"),
    path('privacy_policy',views.privacy_policy, name = "privacy_policy"),
    path('terms_and_conditions',views.terms_and_conditions, name = "terms_and_conditions"),
    # path('contact/',views.contact, name = "contact"),
    path('subscribe', views.subscribe, name='subscribe'),
    
    path('service1', views.service1, name='service1'),
    path('service2', views.service2, name='service2'),
    path('service3', views.service3, name='service3'),
    path('service4', views.service4, name='service4'),
    path('service5', views.service5, name='service5'),
    path('service6', views.service6, name='service6'),
    path('service7', views.service7, name='service7'),
    path('service8', views.service8, name='service8'),

]
