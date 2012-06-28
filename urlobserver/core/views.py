# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html', {})


def add_url(request):
    pass

def check_urls(request):
    pass

def worker_is_dead(request):
    pass
