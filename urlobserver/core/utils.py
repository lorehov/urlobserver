# -*- coding: utf-8 -*-
import urllib


def make_request(worker, remote_url):
    proxies = {'http': 'http://%s:8888' % worker.domain_name}
    fd = urllib.urlopen(remote_url, proxies=proxies)
    return {
        'content': fd.read(),
        'status_code': fd.getcode(),
        'instance_id': worker.instance_id,
    }

def update_urls():
    pass
