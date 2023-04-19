from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic import View

from . import forms
from .League import LEAGUE_CHOICE


class UnauthenticatedOnly(UserPassesTestMixin):
    
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('post:list')

def home(request):
    return render(
        request, 'home.html'
    )

class UserSignUpView(FormView):
    template_name = 'user/signup.html'
    form_class = forms.SignupForm

    def post(self, request, *args, **kwargs):
        user_form = forms.SignupForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            user = authenticate(email=user_form.cleaned_data['email'], password=user_form.cleaned_data['password'])
            login(request, user)
            return redirect('user:detail')
        else:
            print("kkekek")
            return render(request, self.template_name, {'regist_form': self.form_class})


class UserDetailView(LoginRequiredMixin, FormView):
    template_name = 'user/detail.html'
    form_class = forms.DetailForm

    def get(self, request, *arugs, **kwargs):
        return render(request, self.template_name, {'leagues': LEAGUE_CHOICE})

    def post(self, request, *args,**kwargs):
        detail_form = forms.DetailForm(request.POST)
        if detail_form.is_valid():
            user = request.user
            user.username = detail_form.cleaned_data['username']
            user.favorite_league = detail_form.cleaned_data['favorite_league']
            user.content = detail_form.cleaned_data['content'],
            user.save()
            return redirect('post:list')
        else:
            print(detail_form)
            return render(request,self.template_name,{'regist_form':self.form_class})


class UserLoginView(UnauthenticatedOnly ,FormView):
    template_name = 'user/login.html'
    form_class = forms.LoginForm

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('post:list')
        return redirect('user:home')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('user:home')
