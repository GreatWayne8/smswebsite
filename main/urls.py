from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('contact/', views.contact, name='contact'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('about-us/', views.about_us, name='about_us'),
    path('sign-up/', views.sign_up, name='sign_up'),

]
