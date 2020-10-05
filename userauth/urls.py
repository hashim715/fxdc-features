from django.urls import path
from . import views
urlpatterns = [
   path('', views.UserRegisterView, name='register'),
   path('another/', views.another, name='another'),
]