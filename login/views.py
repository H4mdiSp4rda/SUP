# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.shortcuts import render
#from django.http import Http.Response

# Create your views here.
def home(request):
    return render(request, "base.html", {})

def details(request):
    return render(request, "detail.html", {})

def about(request):
    return render(request, "about.html", {})
def contact(request):
    return render(request, "contact.html", {})