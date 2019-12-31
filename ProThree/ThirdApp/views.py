# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def landing(request):
    landing_dict = {'insert_landing': 'Landing Page'}
    return render(request, 'ThirdApp/landing.html', context=landing_dict)
