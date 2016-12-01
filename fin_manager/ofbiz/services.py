import requests
import json

serverRoot = 'http://localhost:8080/finmanager/control'


def getHeaders(request):
    cookie = 'JSESSIONID='+str(request.COOKIES.get('JSESSIONID'))+'; OFBiz.Visitor='+str(request.COOKIES.get('OFBiz.Visitor'))
    headers = {'User-Agent': request.META.get('HTTP_USER_AGENT'),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6','Cache-Control':'max-age=0','Connection':'keep-alive','Host':'localhost:8080','Upgrade-Insecure-Requests':'1','Cookie':cookie}
    return headers

def login(request, webResponse, username, password):
    url = serverRoot + '/doLogin'
    data = {'USERNAME':username, 'PASSWORD':password}
    response = requests.post(url, data=data)

    print("----------------------------------------------------------------------------------------------responce"+str(response.text))

    set_cookies = response.headers.get('Set-Cookie')
    if 'JSESSIONID=' in set_cookies:
        jsessionid = set_cookies[set_cookies.index('JSESSIONID=')+11:]
        webResponse.set_cookie('JSESSIONID',jsessionid[:jsessionid.index(';')])

    if 'OFBiz.Visitor=' in set_cookies:
        visitor = set_cookies[set_cookies.index('OFBiz.Visitor=')+14:]
        webResponse.set_cookie('OFBiz.Visitor',visitor[:visitor.index(';')])
    request.session["username"] = username
    request.session["password"] = password
    ssa = eval(response.text)
    print('haha 1 haha ='+ssa.get('isLoginRight'))
    request.session["isLoginRight"] = response.text[1]

    return response

def register(request, webResponse, username,telNumber,email, password):
    url = serverRoot + '/doRegister'
    data = {'USERNAME':username, 'PASSWORD':password}
    response = requests.post(url, data=data)
    set_cookies = response.headers.get('Set-Cookie')
    if 'JSESSIONID=' in set_cookies:
        jsessionid = set_cookies[set_cookies.index('JSESSIONID=')+11:]
        webResponse.set_cookie('JSESSIONID',jsessionid[:jsessionid.index(';')])

    if 'OFBiz.Visitor=' in set_cookies:
        visitor = set_cookies[set_cookies.index('OFBiz.Visitor=')+14:]
        webResponse.set_cookie('OFBiz.Visitor',visitor[:visitor.index(';')])


def callOfbizService(request, serviceName, postData):
    url = serverRoot + '/' + serviceName
    username = request.session["username"]
    password = request.session["password"]
    postData['login.username'] = username
    postData['login.password'] = password
    print(postData)
    headers = getHeaders(request)
    response = requests.post(url, data=postData, headers=headers)
    return response.json()

def callOfbizNonSecService(serviceName, postData):
    url = serverRoot + '/' + serviceName
    response = requests.post(url, data=postData)
    return response.json()
