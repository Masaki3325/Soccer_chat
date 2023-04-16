from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from . import models
from .League import LEAGUE_CHOICE


user = get_user_model()


class UserSignupForm(forms.ModelForm):
    email = forms.EmailField(label = 'メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
    
    class Meta:
        model = models.User
        fields = ['password','email']

    
class UserDetailForm(forms.ModelForm):
    username = forms.CharField(max_length=50, label = 'ユーザー名')
    favorite_league = forms.ChoiceField(choices=LEAGUE_CHOICE, required=False,widget=forms.Select())
    content = forms.CharField(max_length=500,label = '自己紹介')

    class Meta:
        model = models.User
        fields = ['username','favorite_league','content']


class UserLoginForm(forms.Form):
    email = forms.EmailField(label = 'メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

    class Meta:
        model = models.User
        fields = ['password','email']


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'is_staff', 'is_superuser', 'is_active')

    def clean_password(self):
        return self.initial['password']