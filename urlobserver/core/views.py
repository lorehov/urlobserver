# -*- coding: utf-8 -*-
from django.shortcuts import render
from urlobserver.core.models import Url, Subscriber

#temp import
from django.http import HttpResponse, HttpResponseBadRequest


def index(request):
    return render(request, 'core/index.html', {})

def subscription_add(request):
    #note - this is dognail, change checking realization later
    if not request.method == 'POST':
        return HttpResponseBadRequest("Wrong method")
    post = request.POST
    #@todo: move to model form
    name, callback, url = post.get('name', None), post.get('callback', None), post.get('url', None)
    if not name or not callback or not url:
        return HttpResponseBadRequest("Bad payload")
    subsciber, created = Subscriber.objects.get_or_create(name=name, defaults={'callback': callback})
    url, created = Url.objects.get_or_create(url=url)
    url.subscribers.add(subsciber)
    url.save()
    return HttpResponse("Subscription created")

def subscription_suspend(request):
    pass

def subscription_activate(request):
    pass

def kill_worker(request):
    pass
