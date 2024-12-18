from django.urls import path
from . import views

app_name = 'auth'

urlpatterns = [
	path('', views.AuthView, name='login'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('logout/', views.UserLogout, name='logout'),
	path('dashboard/', views.Dashboard, name='dashboard'),
]

