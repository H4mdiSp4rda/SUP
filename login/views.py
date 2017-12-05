# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.http import Http.Response

# Create your views here.
def home(request):
    return render(request, "base.html", {})
