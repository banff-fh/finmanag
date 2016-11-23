from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^find_invoice/', views.find_invoice, name='find_invoice'),
     url(r'^audit_invoice/', views.audit_invoice, name='audit_invoice'),
     url(r'^create_payment/', views.create_payment, name='create_payment'),
]
