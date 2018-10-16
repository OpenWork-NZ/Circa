# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.http import Http404
from django.db.models import Q

from models import *
from chronos import models as chronos

# Create your views here.
def random_redirect(request):
    return redirect(Photo.random()[0].url())

class AddGroupView(View):
    def get(self, request, photo):
        groups = chronos.Album.objects.all()
        q = request.GET.get("q")
        if q:
            groups = groups.filter(title__icontains = q)
        
        return render(request, "photos/group-search.html", {
            "q" : q,
            "groups" : groups,
            "photo" : get_object_or_404(Photo, slug = photo)
        })

    def post(self, request, photo):
        if "group" not in request.POST: raise Http404("No group provided.")
        photo = get_object_or_404(Photo, slug = photo)
        photo.groups.add(get_object_or_404(chronos.Album, slug = request.POST["group"]))
        return redirect(photo.url())
add_group = AddGroupView.as_view()

class RemoveGroupView(View):
    def get(self, request, photo, group):
        return render(request, "photos/group-delconfirm.html", {
            "photo" : get_object_or_404(Photo, slug = photo),
            "group" : get_object_or_404(chronos.Album, slug = group)
        })

    def post(self, request, photo, group):
        photo = get_object_or_404(Photo, slug = photo)
        group = get_object_or_404(chronos.Album, slug = group)
        photo.groups.remove(group)
        return redirect(photo.url())
remove_group = RemoveGroupView.as_view()

def discover(request):
    return render(request, "photos/discover.html", {
        "photos" : Photo.random(10)
    })
