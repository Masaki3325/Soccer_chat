# Generated by Django 4.1 on 2023-04-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorite_team',
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_league',
            field=models.CharField(choices=[('Premier League', 'Premier League'), ('Bundesliga', 'Bundesliga'), ('La Liga', 'La Liga'), ('Serie A', 'Serie A'), ('Ligue 1', 'Ligue 1'), ('J liague', 'Jリーグ')], default='Jリーグ', max_length=50, verbose_name='好きなリーグ'),
        ),
        migrations.AlterField(
            model_name='user',
            name='content',
            field=models.TextField(max_length=500, verbose_name='自己紹介'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='メールアドレス'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.FileField(upload_to='media/images', verbose_name='プロフィール画像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, verbose_name='ユーザー名'),
        ),
    ]
