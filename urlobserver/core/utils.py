# -*- coding: utf-8 -*-
import urllib
import itertools
from urlobserver.core import models

def _make_response(url, remote_response):
    request = urllib.Request(url)
    request.add_data(remote_response)
    return request

def _make_request(worker, remote_url):
    proxies = {'http': 'http://%s:8888' % worker.domain_name}
    fd = urllib.urlopen(remote_url, proxies=proxies)
    return {
        'content': fd.read(),
        'status_code': fd.getcode(),
        'instance_id': worker.instance_id,
    }

def update_urls():
    workers = itertools.cycle(models.get_workers())
    remote_urls = models.get_urls_to_check()
    for url in remote_urls:
        response = make_request(workers.next(), url)
        for subscriber in url.subscribers:
            urllib.urlopen(_make_response(subscriber.callback, response))
