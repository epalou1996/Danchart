from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from DanchArtApp import views


urlpatterns = [

    path('', views.home, name='home' ),
    path('shop/', views.shop , name='shop'),
    path('galeria/', views.galeria , name='gallery'),
    path('theartist/', views.theartist , name='theartist'),
    path('faq/', views.faq , name='faq'),
    path('proceso/', views.proceso , name='proceso'),
    path('test1/', views.test1 , name='test1'),
    path('test2/', views.test2 , name='test2'),
    

]