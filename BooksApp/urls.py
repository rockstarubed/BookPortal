# BooksApp urls configuration
from django.urls import path,include
from . import views

urlpatterns = [
	path('upload/', views.upload,name='upload'),
	path('viewbooks/', views.viewbooks,name='viewbooks'),
	path('editbook/<int:pk>', views.editbook,name='editbook'),
	path('deletebook/<int:pk>', views.deletebook,name='deletebook'),
]