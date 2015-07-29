# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('friend_id', models.IntegerField(verbose_name='好友ID')),
                ('status', models.IntegerField(verbose_name='状态')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('room_id', models.IntegerField(verbose_name='房间ID')),
                ('topic', models.CharField(max_length=10, verbose_name='游戏主题')),
                ('date', models.DateField(verbose_name='游戏时间')),
                ('duration', models.IntegerField(verbose_name='游戏时长')),
                ('num_players', models.IntegerField(verbose_name='玩家数')),
                ('first_id', models.IntegerField(verbose_name='第一名ID')),
                ('first_score', models.IntegerField(verbose_name='第一名积分')),
                ('second_id', models.IntegerField(verbose_name='第二名ID')),
                ('second_score', models.IntegerField(verbose_name='第二名积分')),
                ('third_id', models.IntegerField(verbose_name='第三名ID')),
                ('third_score', models.IntegerField(verbose_name='第三名积分')),
            ],
        ),
        migrations.CreateModel(
            name='GameQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('game', models.OneToOneField(to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('to_user_id', models.IntegerField(verbose_name='接收用户ID')),
                ('message', models.TextField(max_length=300, verbose_name='消息')),
                ('send_time', models.DateTimeField(verbose_name='发送时间')),
                ('is_read', models.IntegerField(verbose_name='是否阅读')),
                ('from_user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30, verbose_name='昵称')),
                ('head_picture', models.ImageField(upload_to='', verbose_name='头像')),
                ('signature', models.CharField(max_length=200, verbose_name='签名')),
                ('status', models.IntegerField(verbose_name='在线状态')),
                ('integration', models.IntegerField(verbose_name='总积分')),
                ('num_games', models.IntegerField(verbose_name='总游戏数')),
                ('is_forbidden', models.IntegerField(verbose_name='是否禁用账号')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('problem_description', models.TextField(max_length=1000, verbose_name='问题描述')),
                ('problem_type', models.CharField(max_length=10, verbose_name='问题类型')),
                ('num_answer', models.IntegerField(verbose_name='答案数量')),
                ('problem_answer', models.CharField(max_length=1, verbose_name='问题答案')),
                ('answer1', models.TextField(verbose_name='答案1')),
                ('answer2', models.TextField(verbose_name='答案2')),
                ('answer3', models.TextField(verbose_name='答案3')),
                ('answer4', models.TextField(verbose_name='答案4')),
                ('answer5', models.TextField(verbose_name='答案5')),
                ('check_status', models.IntegerField(verbose_name='审核状态')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='gamequestion',
            name='question',
            field=models.OneToOneField(to='game.Question'),
        ),
    ]
