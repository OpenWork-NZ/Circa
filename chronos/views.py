from django.shortcuts import render, get_object_or_404, redirect
from models import Album

# Create your views here.
def date_group(request, group):
    group = get_object_or_404(Album, slug=group)
    if request.method == "GET":
        return render(request, "chronos/date.html", {"group": group})

    if "msg" not in request.POST: return
    start = request.POST["start"] if "has-start" in request.POST else None
    end = request.POST["end"] if "has-end" in request.POST else None
    group.submit_date(request.POST["msg"], start, end,
        request.user, request.POST.get("reference"))

    return redirect(group.url())
