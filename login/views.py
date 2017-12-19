# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.shortcuts import render
#from django.http import Http.Response
from .models import Course
from .forms import AddCourse
# Create your views here.
def home(request):
    return render(request, "base.html", {})

def details(request):
    return render(request, "detail.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})

def test(request):
    return render(request, "sidebar.html", {})

def upload(request):
    form = AddCourse(request.POST or None, request.FILES or None)
    # if form.is_valid():
    #     instance = form.save(commit=False)
    #     instance.save()
    #     message.success(request, "Successfully Created")
    #     return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "upload_form.html", context)