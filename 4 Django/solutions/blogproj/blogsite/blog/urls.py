from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
import blog.views as views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogList.as_view(), name='index'),
    path('post/', views.add_post, name='add_post'),
    # path('post/<int:pk>/', views.BlogDetail.as_view(), name='detail'),
    path('post/<int:pk>/', views.blog_detail, name='detail'),
    path('post/<int:blog_pk>/comment/', views.add_comment, name='add_comment'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),        
]
