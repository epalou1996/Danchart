"""
URL configuration for DanchArt project.

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
#from DanchArt.views import saludo_view, despedida_view
from DanchArt.views import saludo, dar_fecha, calculaEdad, despedida


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/', despedida),
    path('calculaEdad/<int:agno>', calculaEdad),
    path('dar_fecha/', dar_fecha)


    #path(' /', )

    #paths con sistema general
    #('saludo/<str:filename>/', saludo_view, name='saludo'),
    #path('despedida/<str:filename>/', despedida_view, name='despedida'),
]