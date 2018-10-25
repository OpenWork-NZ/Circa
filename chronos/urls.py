from django.conf.urls import include, url
from views import *

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from models import *

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(model=Album)),
    url(r'^(?P<group>[\w-]+)/edit/$', date_group),
]
