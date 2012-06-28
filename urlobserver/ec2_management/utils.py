# -*- coding: utf-8 -*-
"""
To start ec2 instances:

>>> instances = create_ec2_instances()
>>> instance_ids = [instance.id for instance in instances]

To update info about ec2 instances:

>>> for instance in instances:
...    instance.update()

Given instance ids only, get information about instance data:

>>> instances = get_ec2_instances(instance_ids=instance_uds)

To terminate ec2 instances:

>>> get_ec2_connection().terminate_instances(instance_ids)
"""
from boto.ec2.connection import EC2Connection
from django.conf import settings
from django.template.loader import render_to_string


def create_ec2_instances(count=1):
    """
    Launch given number of instances on ec2

    :param count: number of instances to launch

    Function returns the list of instances. Every instance has following list
    of useful properties which could look like following::

        'dns_name': u'ec2-XX-XX-XX-XXX.compute-1.amazonaws.com',
        'id': u'i-XXXXXXX',
        'image_id': u'ami-XXXXXX',
        'instance_type': u't1.micro',
        'ip_address': u'23.21.XX.XX',
        'launch_time': u'2012-06-28T05:37:37.000Z',
        'private_dns_name': u'ip-10-XX-XX-XX.ec2.internal',
        'private_ip_address': u'10.XX.XX.XX',
        'public_dns_name': u'ec2-XX-XX-XX-XX.compute-1.amazonaws.com',
        'state': 'running',
        'state_code': 16,

    At the moment of return every almost nothing is filled with real data, and
    has None in its values, so to get more information, it is required to
    perform ``instance.update()`` for every instance.
    """
    conn = get_ec2_connection()
    user_data = get_user_data()
    reservation = conn.run_instances(image_id=settings.EC2_IMAGE_ID,
                                     min_count=count,
                                     max_count=count,
                                     instance_type=settings.EC2_INSTANCE_TYPE,
                                     user_data=user_data)
    return reservation.instances


def get_user_data():
    """
    Create user_data text message to start up a new ubuntu service

    It can be a simple shell script, config or even a multi-part message

    Function which on a basis of pre-defined parametes creates a multipart
    message suitable to start up a new Ubuntu image

    See https://help.ubuntu.com/community/CloudInit for details
    """
    context = {
            'ssh_public_keys': settings.EC2_SSH_PUBLIC_KEYS,
            'allowed_ips': settings.EC2_ALLOWED_IPS,
    }
    return render_to_string('ec2_management/init.sh', context)


def get_ec2_instances(instance_ids=None):
    """
    Given a list of instance ids, return list of instance objects

    If instance_ids is None, then return all available instances
    """
    instances = []
    conn = get_ec2_connection()
    result_set = conn.get_all_instances()
    for reservation in result_set:
        instances += reservation.instances
    return instances


def get_ec2_connection():
    conn = EC2Connection(settings.AWS_ACCESS_KEY, settings.AWS_SECRET)
    return conn
