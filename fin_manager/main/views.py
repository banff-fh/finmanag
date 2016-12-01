from django.shortcuts import render,render_to_response
from django.http import JsonResponse
import requests
from ofbiz import services
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms

serverRoot = 'http://localhost:8080/finmanager/control'

class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

# Home
def home(request):
    return render(request,'index.html',{})
# Login Layout
def login(request):
    username = request.COOKIES.get('isLoginRight', '')
    return render_to_response('login_v2.html', {'isLoginRight': username})
# Call Login Service
def doLogin(req):

        if req.method == 'POST':
            uf = UserForm(req.POST)
            if uf.is_valid():
                # 获取表单用户密码
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                # 获取的表单数据与数据库进行比较
                #user = User.objects.filter(username__exact=username, password__exact=password)
                url = serverRoot + '/doLogin'
                data = {'USERNAME': username, 'PASSWORD': password}

                response = requests.post(url, data=data)
                print("--------------------------------------------------------------------------"+response.text)
                user = eval(response.text);
                if user:
                    # 比较成功，跳转index
                    response = HttpResponseRedirect('/main/login/')
                    # 将username写入浏览器cookie,失效时间为3600
                    response.set_cookie('isLoginRight', user.get('_ERROR_MESSAGE_'), 3600)
                    return response
                else:
                    # 比较失败，还在login
                    return HttpResponseRedirect('/main/login/')
        else:
            uf = UserForm()
        return render_to_response('login_v2.html', {'uf': uf}, context_instance=RequestContext(req))

    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # webResponse = render(request,'login_v2.html',{})
    # services.login(request, webResponse, username, password)
    # return webResponse
