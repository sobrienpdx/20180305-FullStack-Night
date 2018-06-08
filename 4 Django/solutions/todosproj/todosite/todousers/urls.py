from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'todousers'
urlpatterns = [
	path('', views.index, name='index'),
	path('add/', views.add, name='add'),
	path('<int:pk>/delete/', views.delete, name='delete'),
	path('<int:pk>/mark/', views.toggle_done, name='mark'),
	path('signup/', views.signup, name='signup'),
	path('login/', auth_views.LoginView.as_view(),  name='login'), 
	path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
	]