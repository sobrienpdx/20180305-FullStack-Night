from django.urls import path
from django.conf import settings
from . import views

app_name = 'todovue'
urlpatterns = [
	# path('', views.IndexView.as_view(), name='index'),
	# path('add/', views.add, name='add'),
	# path('<int:pk>/delete/', views.delete, name='delete'),
	# path('<int:pk>/mark/', views.toggle_done, name='mark'),
]