from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class PostListView(TemplateView):
    template_name = 'post/list.html'