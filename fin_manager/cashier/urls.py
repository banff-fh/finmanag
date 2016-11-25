from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^find_invoice/', views.find_invoice, name='find_invoice'),
     url(r'^audit_invoice/', views.audit_invoice, name='audit_invoice'),
     url(r'^create_invoice/', views.create_invoice, name='create_invoice'),
     url(r'^update_invoice_status/', views.update_invoice_status, name='update_invoice_status'),
     url(r'^create_invoice_item/', views.create_invoice_item, name='create_invoice_item'),
]
