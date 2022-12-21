from django.urls import path,re_path
from Second_App import views

urlpatterns=[
		path('third/',views.f3),
		path('fourth/', views.f4),
];
