"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from FirstApp import views
from Second_App import views as v1
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('django/',views.display),
    path('wel/',views.show),
    path('time/',v1.f11),
    path('welcome/',views.display),
    
    path('FirstApp/',include("FirstApp.urls")),
    path('Second_App/',include("Second_App.urls")),
    path('dtime/',v1.senddatetime),
    
    re_path('^.*$',views.show),
];
