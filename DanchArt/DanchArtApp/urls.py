from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from DanchArtApp import views


urlpatterns = [

    path('', views.home, name='home' ),
    path('shop/', views.shop , name='shop'),
    

]