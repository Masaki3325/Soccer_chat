from django.db import models

# Create your models here.

class Accountinfo(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, help_text='有効なメールアドレスを入力してください')
    
