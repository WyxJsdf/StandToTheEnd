# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from PIL import Image
from django.contrib import auth
import datetime
from game.models import Player


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username, password = password)
        if user is not None and user.is_active:
            auth.login(request, user)
            check = request.POST.get('check', '')
            if check == 'on':
                dt = datetime.datetime.now() + datetime.timedelta(weeks = 3)
                response = HttpResponseRedirect('/')
                response.set_cookie("username", username, expires=dt)
                return response
            else:
                if request.user.is_staff:
                    return HttpResponseRedirect('/gamehall')
                else:
                    return HttpResponseRedirect('/gamehall')
        elif user is not None:
            errors = u'该账户已被禁用!'
            return render_to_response("index.html", {'error1': errors}, context_instance=RequestContext(request))
        else:
            errors = u'用户名或密码错误!'
            return render_to_response("index.html", {'error1': errors}, context_instance=RequestContext(request))
    else:
        if request.user.is_authenticated():
            if request.user.is_staff:
                return HttpResponseRedirect('/gamehall')
            else:
                return HttpResponseRedirect('/gamehall')
        if 'username' in request.COOKIES:
            user = User.objects.get(username = request.COOKIES['username'])
            auth.login(request, user)
            if request.user.is_staff:
                return HttpResponseRedirect('/gamehall')
            else:
                return HttpResponseRedirect('/gamehall')
        return render_to_response('index.html', context_instance=RequestContext(request))


def register(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    repassword = request.POST.get('repassword','')
    email = request.POST.get('email','')
    nickname = request.POST.get('nickname','')
    if (username == ''):
        errors = '请输入您的密码'
        return render_to_response("index.html", {'message':'register','error2': errors}, context_instance=RequestContext(request))
    try:
        p = User.objects.get(username = username)
    except User.DoesNotExist:
        if (password != repassword):
            errors = '两次输入密码不一致，请重新输入'
            return render_to_response("index.html", {'message':'register','error2': errors}, context_instance=RequestContext(request))
        if (len(password) < 6):
            errors = '密码长度太短，请重新输入'
            return render_to_response("index.html", {'message':'register','error2': errors}, context_instance=RequestContext(request))
        if nickname == '':
            errors = '请输入您的昵称'
            return render_to_response("index.html", {'message':'register','error2': errors}, context_instance=RequestContext(request))
        if email == '':
            errors = '请输入您的邮箱'
            return render_to_response("index.html", {'message':'register','error2': errors}, context_instance=RequestContext(request))
        user = User.objects.create_user(username = username,email = email,password = password)
        user.save()
        player = Player(user = user, nickname = nickname, signature = '', integration = 0, num_games = 0, is_forbidden = 0, status = 1)
        player.save()
        user = user = auth.authenticate(username = username, password = password)
        auth.login(request, user)
        return HttpResponseRedirect('/gamehall')
    else:
        errors = '用户名已被注册'
        return render_to_response("index.html", {'message':'register','error2': errors}, context_instance=RequestContext(request))


def gamehall(request):
    return  render_to_response('game/profile.html', context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    response.delete_cookie("username")
    return response


def myUserInfo(request):
    if request.method == 'POST':
        if 'changePassword' in request.POST:
            old_password = request.POST.get("old_password", "")
            new_password = request.POST.get("new_password", "")
            confirm_password = request.POST.get("re_password", "")
            if new_password != confirm_password:
                return HttpResponse("修改失败，新密码不一致！")
            elif len(new_password) < 6:
                return HttpResponse("修改失败，密码太短！")
            user = auth.authenticate(username=request.user.username, password=old_password)
            if user is not None:
                user.set_password(new_password)
                user.save()
                return HttpResponse("密码修改成功！")
            else:
                return HttpResponse("修改失败，旧密码错误！")
    else:
        return  render_to_response('game/profile.html', context_instance=RequestContext(request))


def change_password(request):
    old_password = request.POST.get("old_password", "")
    new_password = request.POST.get("new_password", "")
    confirm_password = request.POST.get("re_password", "")
    if new_password != confirm_password:
        return HttpResponse("修改失败，新密码不一致！")
    elif len(new_password) < 6:
        return HttpResponse("修改失败，密码太短！")
    user = auth.authenticate(username=request.user.username, password=old_password)
    if user is not None:
        user.set_password(new_password)
        user.save()
        return HttpResponse("密码修改成功！")
    else:
        return HttpResponse("修改失败，旧密码错误！")

# def upload(request):
#     reqfile = request.FILES['picfile']
#     img = Image.open(reqfile)
#     img.save("a.png","png")
#     return render_to_response('index.html', context_instance=RequestContext(request))