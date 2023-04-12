from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.UserSignUpView.as_view(),name='signup'),
    path('detail/', views.UserDetailView.as_view(),name='detail'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/', views.UserLogoutView.as_view(),name='logout'),
]