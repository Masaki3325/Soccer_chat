from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic import View

from . import forms
from .League import LEAGUE_CHOICE
# Create your views here.


class UnauthenticatedOnly(UserPassesTestMixin):
    """
    ログイン済みのユーザーのアクセスを制限する
    """
    def test_func(self):
        # ログイン状態じゃないかチェック
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        # ログイン済みならregist_success_viewにリダイレクト
        return redirect('accounts:regist_success_view')

def home(request):
    return render(
        request, 'home.html'
    )

class UserSignUpView(FormView):
    template_name = 'user/signup.html'
    form_class = forms.UserSignupForm

    def post(self, request, *args, **kwargs):
        user_form = forms.UserSignupForm(request.POST)
        
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
    form_class = forms.UserDetailForm

    def get(self, request, *arugs, **kwargs):
        return render(request, self.template_name, {'leagues': LEAGUE_CHOICE})

    def post(self, request, *args,**kwargs):
        detail_form = forms.UserDetailForm(request.POST)
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
    form_class = forms.UserLoginForm

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
