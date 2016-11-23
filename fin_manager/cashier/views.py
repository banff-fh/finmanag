from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# find invoice item layout
def find_invoice(request):
    return render(request,'find_invoice.html',{})

# audit invoice layout
def audit_invoice(request):
    return render(request,'audit_invoice.html',{})

# create payment
def create_payment(request):
    return render(request,'create_payment.html',{})