from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('list/', views.PostListView.as_view(),name='list')
]