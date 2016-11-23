from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def find_invoice(request):
    return render(request,'find_invoice.html',{})

