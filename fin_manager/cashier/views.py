from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# find invoice item layout
def find_invoice(request):
    return render(request,'find_invoice.html',{})

# audit invoice layout
def audit_invoice(request):
    return render(request,'audit_invoice.html',{})

# create invoice layout
def create_invoice(request):
    return render(request, 'create_invoice.html', {})

# update invoice status layout
def update_invoice_status(request):
    return render(request, 'update_invoice_status.html', {})

# create invoice item
def create_invoice_item(request):
    return render(request, 'create_invoice_item.html', {})

