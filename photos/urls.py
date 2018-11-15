from django.conf.urls import include, url
from views import *

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from models import *

urlpatterns = [
    url(r'^random/$', random_redirect),
    url(r'^add/$', add_photo),
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(model=Photo)),
    url(r'^(?P<photo>[\w-]+)/groups/add/$', add_group),
    url(r'^(?P<photo>[\w-]+)/groups/add/new/$', new_group),
    url(r'^(?P<photo>[\w-]+)/groups/(?P<group>[\w-]+)/remove/$', remove_group)
]
