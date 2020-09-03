from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from MyApp.models import *

@login_required
def welcome(request):
    # return HttpResponse("欢迎来到主页")
    return render(request,'welcome.html')


def case_list(request):
    return render(request,'caselist.html')

@login_required
def home(request):
    return render(request,'welcome.html',{"whichHTML":"home.html","oid":""})

def child(request,eid,oid):
    return render(request,eid)

def login(request):
    return render(request,'login.html')

def login_action(request):
    u_nmae=request.GET['username']
    p_word=request.GET['password']

    #开始联通django用户库，查看用户名密码是否正确

    user=auth.authenticate(username=u_nmae,password=p_word)
    if user is not None:
        # return HttpResponseRedirect('/home/')
        auth.login(request,user)
        request.session['user']=u_nmae
        return HttpResponse('成功')
    else:
        return HttpResponse('失败')

def register_action(request):
    u_nmae = request.GET['username']
    p_word = request.GET['password']
    #开始联通django用户表

    try:
        user=User.objects.create_user(username=u_nmae,password=p_word)
        user.save()
        return HttpResponse("恭喜,注册成功！")
    except:
        return HttpResponse("注册失败,用户名可能已经存在")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

def pei(request):
    tucao_test=request.GET['tucao_text']
    DB_tucao.objects.create(user=request.user.username,text=tucao_test)
    return HttpResponse("")

def api_help(request):
    return render(request,"welcome.html",{"whichHTML":"help.html","oid":""})



