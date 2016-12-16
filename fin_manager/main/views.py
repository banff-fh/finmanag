from django.core.paginator import PageNotAnInteger, EmptyPage
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
import requests

from ofbiz import services
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms

serverRoot = 'http://localhost:8080/finmanager/control'


class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())


# Home
def home(request, *args, **kwargs):
 viewindex = request.GET.get('viewindex', '0')
 viewsize = request.GET.get('viewsize', '2')
 nikename = request.session.get('nikename')
 username = request.session.get('username')
 password = request.session.get('password')
 if nikename != None:

    return render(request, 'index.html', {'nikename': nikename, 'username': username})
 else:
    return render(request, 'login_v2.html')


# Login Layout
def login(request):
    nikename = request.session.get('nikename')

    if nikename != None:
        return render(request, 'index.html', {'nikename': nikename})
    else:
        msg = request.session.get('errormessage')
        return render(request, 'login_v2.html', {'errormessage': msg})


# Call Login Service
def doLogin(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较

            url = serverRoot + '/doLogin'

            data = {'username': username, 'password': password}
            response = requests.post(url, data=data)
            user = eval(response.text);
            print('老金请看返回格式'+response.text)
            if user.get('nikename'):
                # 比较成功，跳转index
                response = HttpResponseRedirect('/main/home/')
                # 将username写入浏览器cookie,失效时间为3600
                req.session["username"] = username
                req.session["password"] = password
                req.session["nikename"] = user.get('nikename')
                response.set_cookie('username', username, 3600)
                return response
            else:
                # 比较失败，还在login
                # return render_to_response('/main/login/', {'errormessage':  user.get('_ERROR_MESSAGE_')})
                req.session["errormessage"] = user.get('_ERROR_MESSAGE_')
                return HttpResponseRedirect('/main/login/')
    else:
        uf = UserForm()
    return render_to_response('login_v2.html', {'uf': uf}, context_instance=RequestContext(req))

    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # webResponse = render(request,'login_v2.html',{})
    # services.login(request, webResponse, username, password)
    # return webResponse


def logout(request):
    request.session["nikename"] = '';
    return render_to_response('login_v2.html')
