from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# find invoice item layout
def find_party(request):
    return render(request,'find_party.html',{})
def create_party(request):
    return render(request,'create_party.html',{})