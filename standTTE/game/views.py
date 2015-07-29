# coding: utf-8
from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User


def hello(request):
    return render_to_response('index.html', context_instance=RequestContext(request))