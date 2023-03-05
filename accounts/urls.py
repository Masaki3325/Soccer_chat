from django.contrib import admin
from django.urls import path
from .views import signup, login

urlpatterns = [
   path('sigunp/',signup.as_view(),name='signup'),
   path('login/',login.as_view(),name='login'),
]