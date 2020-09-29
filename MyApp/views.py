from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from MyApp.models import *
import json,requests

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
    res=child_json(eid,oid)   #对应每个子页面返回的内容
    return render(request,eid,res)

def child_json(eid,oid=''):
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
    if eid=="P_apis.html":
        project=DB_project.objects.filter(id=oid)[0]
        res={"project":project}
    if eid=="P_cases.html":
        project=DB_project.objects.filter(id=oid)[0]
        res={"project":project}
    if eid=="P_project_set.html":
        project=DB_project.objects.filter(id=oid)[0]
        res={"project":project}
    if eid=="P_apis.html":
        project=DB_project.objects.filter(id=oid)[0]
        apis=DB_apis.objects.filter(project_id=oid)
        res={"project":project,"apis":apis}
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
    DB_apis.objects.filter(project_id=id).delete()  #删除项目的同时，删除项目中创建的接口
    return HttpResponse("")

def add_project(request):
    project_name=request.GET['project_name']
    DB_project.objects.create(name=project_name,remark="",user=request.user.username,other_users='')
    return HttpResponse("")

def open_apis(request,id):
    """进入接口库"""
    project_id=id
    return render(request,'welcome.html',{"whichHTML":"P_apis.html","oid":project_id})

def open_cases(request,id):
    """进入用例设置库"""
    project_id=id
    return render(request,'welcome.html',{"whichHTML":"P_cases.html","oid":project_id})

def open_project_set(request,id):
    """进入项目设置"""
    project_id=id
    return render(request,'welcome.html',{"whichHTML":"P_project_set.html","oid":project_id})

#保存项目设置
def save_project_set(request,id):
    project_id=id
    name=request.GET['name']
    remark=request.GET['remark']
    other_user=request.GET['other_user']
    DB_project.objects.filter(id=project_id).update(name=name,remark=remark,other_users=other_user)
    return HttpResponse('')

#保存备注
def save_bz(request):
    api_id=request.GET['api_id']
    bz_value=request.GET['bz_value']
    DB_apis.objects.filter(id=api_id).update(des=bz_value)
    return HttpResponse("")

#获取备注
def get_bz(request):
    api_id = request.GET['api_id']
    bz_value=DB_apis.objects.filter(id=api_id)[0].des
    return HttpResponse(bz_value)

#保存接口
def Api_save(request):
    #提前所有数据
    api_id=request.GET['api_id']
    api_name=request.GET['api_name']
    ts_method=request.GET['ts_method']
    ts_url=request.GET['ts_url']
    ts_host=request.GET['ts_host']
    ts_header=request.GET['ts_header']
    ts_body_method=request.GET['ts_body_method']
    if ts_body_method=="返回体":
        api=DB_apis.objects.filter(id=api_id)[0]
        ts_body_method=api.last_body_method
        ts_api_body=api.last_api_body

    else:
        ts_api_body = request.GET['ts_api_body']

    #保存数据
    DB_apis.objects.filter(id=api_id).update(
        api_method=ts_method,
        api_url=ts_url,
        api_header=ts_header,
        api_host=ts_host,
        body_method=ts_body_method,
        api_body=ts_api_body,
        name=api_name
    )

    #返回
    return HttpResponse('success')

#获取接口数据
def get_api_data(request):
    api_id=request.GET['api_id']
    api=DB_apis.objects.filter(id=api_id).values()[0]
    return HttpResponse(json.dumps(api),content_type='application/json')

#调试层发送请求
def Api_send(request):
    #提取所有数据
    api_id=request.GET['api_id']
    ts_method=request.GET['ts_method']
    ts_url=request.GET['ts_url']
    ts_host=request.GET['ts_host']
    ts_header=request.GET['ts_header']
    api_name=request.GET['api_name']
    ts_body_method = request.GET['ts_body_method']
    print(ts_body_method)
    if ts_body_method=="返回体":
        api=DB_apis.objects.filter(id=api_id)[0]
        ts_body_method=api.last_body_method
        ts_api_body=api.last_api_body

        if ts_body_method in ['',None]:
            return HttpResponse("请先选择请求体编码格式和请求体，再点击send按钮发送请求")
    else:
        ts_api_body=request.GET['ts_api_body']
        api=DB_apis.objects.filter(id=api_id)
        api.update(last_body_method=ts_body_method,last_api_body=ts_api_body)

    #发送请求获取返回值
    header=json.loads(ts_header)

    #拼接完整url
    if ts_host[-1] == '/' and ts_url[0]=='/':
        url=ts_host[:-1]+ts_url
    elif ts_host[-1] !='/' and ts_url[0] !='/':
        url=ts_host+'/'+ts_url
    else:
        url=ts_host+ts_url

    if ts_body_method=='none':
        response=requests.request(ts_method.upper(),url,headers=header,data={})

    elif ts_body_method=="form-data":
        files=[]
        payload={}
        for i in eval(ts_api_body):
            payload[i[0]]=i[1]
        response=requests.request(ts_method.upper(),url,headers=header,data=payload,files=files)

    elif ts_body_method=='x-www-form-urlencoded':
        header['content-type']='application/x-www-form-urlencoded'
        payload={}
        for i in eval(ts_api_body):
            payload[i[0]] = i[1]
            response = requests.request(ts_method.upper(), url, headers=header, data=payload)

    else: #这时肯定是raw的5个子选项
        if ts_body_method=='Text':
            header['content-type'] = 'text/plain'
        if ts_body_method=='JavaScript':
            header['content-type'] = 'text/plain'
        if ts_body_method=='Json':
            header['content-type'] = 'text/plain'
        if ts_body_method=='Html':
            header['content-type'] = 'text/plain'
        if ts_body_method=='Xml':
            header['content-type'] = 'text/plain'
        response = requests.request(ts_method.upper(), url, headers=header, data=ts_api_body.encode('utf-8'))


    #把返回值传递给前端页面
    return HttpResponse(response.text)

