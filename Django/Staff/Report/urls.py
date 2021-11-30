from  django.urls import path 

from . import views

urlpatterns = [

	path('',views.home, name='home'),
	path('new', views.employeeDetails, name = 'employeeDetails'),
	path('display', views.displayDetails, name='displayDetails'),
	path('added/', views.thanks, name='thanks')
]