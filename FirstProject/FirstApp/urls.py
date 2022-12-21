from django.urls import path,re_path
from FirstApp import views

urlpatterns=[
		path('first/',views.f1),
		path('second/',views.f2),
];