from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import blog.views as views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogList.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),        
]
