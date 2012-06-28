import itertools
import urllib2

from urlobserver.core import models

def _make_response(url, remote_response):
    request = urllib2.Request(url)
    request.add_data(remote_response)
    return request

def update_urls():
    workers = itertools.cycle(models.get_workers())
    remote_urls = models.get_urls_to_check()
    for url in remote_urls:
        response = make_request(workers.next(), url)
        for subscriber in url.subscribers:
            urllib2.urlopen(_make_response(subscriber.callback, response))

def make_request(worker, remote_url):
    pass
