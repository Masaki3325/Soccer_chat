from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from .League import LEAGUE_CHOICE
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('メールアドレスを必ず入力してください')
        elif not username:
            raise ValueError('名前を入力してください')
        user = self.model(
            username = username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50,verbose_name = 'ユーザー名')
    email = models.EmailField(max_length=255, unique=True,verbose_name = 'メールアドレス')
    favorite_league = models.CharField(max_length=50, choices=LEAGUE_CHOICE, default='Jリーグ', verbose_name = '好きなリーグ')
    content = models.CharField(max_length=500,verbose_name = '自己紹介')
    image = models.FileField(upload_to='media/images',verbose_name = 'プロフィール画像')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 
    
    objects = UserManager()
    
    class Meta:
        db_table = 'user'