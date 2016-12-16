from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import requests

serverRoot = 'http://localhost:8080/finmanager/control'

# find invoice item layout
def find_invoice(request):
    viewindex      = request.GET.get('viewindex', '0')
    viewsize       = request.GET.get('viewsize', '2000')
    invoice_status = request.POST.get('invoice_status')
    user_name      = request.POST.get('username')
    nikename = request.session.get('nikename')
    username = request.session.get('username')
    password = request.session.get('password')


    if nikename:
        url = serverRoot + '/findInvoiceDetail'
        if invoice_status:
            print("----------request scope form value = " + invoice_status)
        data = {'entityname': "Invoice", 'username': username, 'password': password, 'viewindex': viewindex,
                'viewsize':viewsize,"invoice_status":invoice_status,"user_name":user_name}
        response = requests.post(url, data=data)
        jsonData = response.json()
        object_list = []
        object_list   = jsonData['returnList']

        return render(request, 'find_invoice.html', {'nikename': nikename, 'username': username,'list':object_list,'response':response.text,'viewindex':viewindex})
    else:
        return render(request, 'login_v2.html')

# audit invoice layout
def audit_invoice(request):
    viewindex = request.GET.get('viewindex', '0')
    viewsize = request.GET.get('viewsize', '50')
    nikename = request.session.get('nikename')
    username = request.session.get('username')
    password = request.session.get('password')
    if nikename:

        url = serverRoot + '/posPerFormFind'
        data = {'entityname': "Invoice", 'username': username, 'password': password, 'viewindex': viewindex,
                'viewsize': viewsize}
        response = requests.post(url, data=data)
        jsonData = response.json()
        object_list = []
        object_list = jsonData['returnList']

        return render(request, 'audit_invoice.html',
                      {'nikename': nikename, 'username': username, 'list': object_list, 'response': response.text,
                       'viewindex': viewindex})
    else:
        return render(request, 'login_v2.html')


# create invoice layout
def create_invoice(request):
    viewindex = request.GET.get('viewindex', '0')
    viewsize = request.GET.get('viewsize', '500')
    nikename = request.session.get('nikename')
    username = request.session.get('username')
    password = request.session.get('password')
    if nikename:

        url = serverRoot + '/posPerFormFind'
        data = {'entityname': "PartyAndUserLoginAndPerson", 'username': username, 'password': password,
                'viewindex': viewindex,
                'viewsize': viewsize}
        response = requests.post(url, data=data)
        jsonData = response.json()
        object_list = []
        object_list = jsonData['returnList']

        return render(request, 'create_invoice.html',
                      {'nikename': nikename, 'username': username, 'list': object_list, 'response': response.text,
                       'viewindex': viewindex})
    else:
        return render(request, 'login_v2.html')


# update invoice status layout
def update_invoice_status(request):
    viewindex = request.GET.get('viewindex', '0')
    viewsize = request.GET.get('viewsize', '50')
    nikename = request.session.get('nikename')
    username = request.session.get('username')
    password = request.session.get('password')
    if nikename:

        url = serverRoot + '/posPerFormFind'
        data = {'entityname': "Invoice", 'username': username, 'password': password,
                'viewindex': viewindex,
                'viewsize': viewsize}
        response = requests.post(url, data=data)
        jsonData = response.json()
        object_list = []
        object_list = jsonData['returnList']

        return render(request, 'update_invoice_status.html',
                      {'nikename': nikename, 'username': username, 'list': object_list, 'response': response.text,
                       'viewindex': viewindex})
    else:
        return render(request, 'login_v2.html')


# create invoice item
def create_invoice_item(request):
    return render(request, 'create_invoice_item.html', {})

