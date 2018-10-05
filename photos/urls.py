from django.conf.urls import include, url
from views import *

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from models import *

urlpatterns = [
    url(r'^random/', random_redirect),
    url(r'^new/', CreateView.as_view(model=Photo),
    url(r'^<slug:slug>/', DetailView.as_view(model=Photo)),
    url(r'^<slug:photo>/groups/add/$', add_group),
    url(r'^<slug:photo>/groups/<slug:group>/remove/$', remove_group)
]
