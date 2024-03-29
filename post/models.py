from django.db import models
from django.contrib.auth import get_user_model

from user import League


User = get_user_model()


class Common(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("投稿者"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=('投稿日'))

    class Meta:
        abstract = True



class Team(models.Model):
    league = models.CharField(max_length=50, choices=League.LEAGUE_CHOICE, verbose_name=('リーグ'))
    logo = models.ImageField(upload_to='image/', verbose_name=('エンブレム'))
    location = models.CharField(max_length=150, verbose_name=('本拠地'))
    temaname = models.CharField(max_length=50, verbose_name=('チームネーム'))
    content = models.CharField(max_length=300, verbose_name=('チーム紹介'))

    def __str__(self):
        return self.temaname


class Post(Common):
    title = models.CharField(max_length=50, default='タイトルC', verbose_name=('タイトル'))
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, verbose_name=("チーム"))
    content = models.CharField(max_length=140, verbose_name=('投稿内容'))

    def __str__(self):
        return self.title

   
class Comment(Common):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commented_post", verbose_name=("投稿"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("投稿者"))
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name=('投稿日'))
    content = models.CharField(max_length=80, verbose_name=('投稿内容'))

    def __str__(self):
        return self.content