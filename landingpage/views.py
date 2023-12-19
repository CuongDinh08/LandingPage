from django.http.request import HttpRequest
from django.shortcuts import render
from django.conf import settings


def view_landing_page(request: HttpRequest):
    context = {"landingpage_title": getattr(settings, "SERVER_NAME", "Primary server")}
    return render(request, "index.html", context)
