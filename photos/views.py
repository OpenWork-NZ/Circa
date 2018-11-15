# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.http import Http404
from django.db.models import Q
from django.utils.text import slugify

from django.contrib.auth import authenticate

from models import *
from chronos import models as chronos
from forms import UploadPhotoForm

# Create your views here.
def random_redirect(request):
    return redirect(Photo.random()[0].url())

def add_photo(request):
    if request.method == "POST":
        form = UploadPhotoForm(request.POST)
        user = authenticate(form.cleaned_data['username'],
                            form.cleaned_data['password'])
        if form.is_valid() and (
                user is not None and user.has_perm('photos.add_photo')):
            photo = Photo(src=form.cleaned_data['link'],
                        title=form.cleaned_data['title'],
                        alt=form.cleaned_data['description'],
                        slug=slugify(form.cleaned_data['title'], allow_unicode=True))
            photo.save()
            return redirect(photo.url())
    else:
        form = UploadPhotoForm()
    return render(request, "photos/photo_form.html", {"form" : form})

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

def new_group(request, photo):
    if "name" not in request.POST: raise Http404("No name POSTed.")
    photo = get_object_or_404(Photo, slug = photo)
    name = request.POST["name"]
    album = Album(title = name, slug = slugify(name))
    album.save()
    photo.groups.add(album)
    return redirect(photo.url())

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
