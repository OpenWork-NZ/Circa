from django.conf.urls import include, url
from views import *

from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from models import *

urlpatterns = [
    url(r'^<slug:slug>/$', DetailView.as_view(model=Album)),
    url(r'^<slug:slug>/edit/$', UpdateView.as_view(model=Album,
            fields=["title", "description", "href", "start", "end"]),
            success_url = ".."),
]
