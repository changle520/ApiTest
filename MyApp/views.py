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
    res=child_json(eid)
    return render(request,eid,res)

def child_json(eid):
    '''
    数据分发器：控制不同的页面返回不同的数据
    :param eid:
    :return:
    '''
    res={}
    if eid=='home.html':
        data=DB_home_href.objects.all()
        res={"hrefs":data}
    if eid=="project_list.html":
        data=DB_project.objects.all()
        res={"projects":data}
    return res

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

def project_list(request):
    return render(request,'welcome.html',{"whichHTML":"project_list.html","oid":""})

def delete_project(request):
    id=request.GET['id']
    DB_project.objects.filter(id=id).delete()
    return HttpResponse("")

def add_project(request):
    project_name=request.GET['project_name']
    DB_project.objects.create(name=project_name,remark="",user=request.user.username,other_users='')
    return HttpResponse("")




