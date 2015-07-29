# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(u'昵称', max_length=30)
    head_picture = models.ImageField(u'头像')
    signature = models.CharField(u'签名', max_length=200)
    status = models.IntegerField(u'在线状态')
    integration = models.IntegerField(u'总积分')
    num_games = models.IntegerField(u'总游戏数')
    is_forbidden = models.IntegerField(u'是否禁用账号')


class Friend(models.Model):
    user = models.OneToOneField(User)
    friend_id = models.IntegerField(u'好友ID')
    status = models.IntegerField(u'状态')


class Message(models.Model):
    from_user = models.OneToOneField(User)
    to_user_id = models.IntegerField(u'接收用户ID')
    message = models.TextField(u'消息', max_length=300)
    send_time = models.DateTimeField(u'发送时间')
    is_read = models.IntegerField(u'是否阅读')


class Question(models.Model):
    user = models.OneToOneField(User)
    problem_description = models.TextField(u'问题描述', max_length=1000)
    problem_type = models.CharField(u'问题类型', max_length=10)
    num_answer = models.IntegerField(u'答案数量')
    problem_answer = models.CharField(u'问题答案', max_length=1)
    answer1 = models.TextField(u'答案1')
    answer2 = models.TextField(u'答案2')
    answer3 = models.TextField(u'答案3')
    answer4 = models.TextField(u'答案4')
    answer5 = models.TextField(u'答案5')
    check_status = models.IntegerField(u'审核状态')


class Game(models.Model):
    room_id = models.IntegerField(u'房间ID')
    topic = models.CharField(u'游戏主题', max_length=10)
    date = models.DateField(u'游戏时间')
    duration = models.IntegerField(u'游戏时长')
    num_players = models.IntegerField(u'玩家数')
    first_id = models.IntegerField(u'第一名ID')
    first_score = models.IntegerField(u'第一名积分')
    second_id = models.IntegerField(u'第二名ID')
    second_score = models.IntegerField(u'第二名积分')
    third_id = models.IntegerField(u'第三名ID')
    third_score = models.IntegerField(u'第三名积分')


class GameQuestion(models.Model):
    game = models.OneToOneField(Game)
    question = models.OneToOneField(Question)