from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('list/', views.PostListView.as_view(),name='list'),
    path('detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('delete/<int:pk>', views.PostDeleteView.as_view(), name='delete'),
]