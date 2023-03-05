from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm


# Create your views here.

class signup(CreateView):
    form_class = SignUpForm
    template_name = "signup.html" 
    success_message = 'アカウント作成に成功しました'
    success_url = reverse_lazy('')

class login():

