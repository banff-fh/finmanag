from django.conf.urls import url
from . import views

urlpatterns = [
#find_party_layout
url(r'^find_party', views.find_party, name='find_party'),
#create_party_layout
url(r'^create_party', views.create_party, name='create_party'),
]
