#UserApp url configuration

from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('about/',views.about, name='about'),
    path('feedback/',views.feedback, name='feedback'),
]
