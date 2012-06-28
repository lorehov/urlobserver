import random

from django.db import models
from urlobserver import localsettings

SUBSCRIBER_ACTIVE = 0
SUBSCRIBER_SUSPENDED = 1
SUBSCRIBER_DELETED = 2

# Create your models here.
class Subscriber(models.Model):
    status = models.SmallIntegerField(choices=[
        (SUBSCRIBER_ACTIVE, "Active"),
        (SUBSCRIBER_SUSPENDED, "Suspended"),
        (SUBSCRIBER_DELETED, "Deleted")
    ])

    name = models.CharField(max_length=255)
    callback = models.CharField(max_length=1000)

class Worker(models.Model):
    instance_id = models.CharField(max_length=255)
    domain_name = models.CharField(max_length=1000)

class Url(models.Model):
    subscribers = models.ManyToManyField(Subscriber)

    url = models.CharField(max_length=1000)
    sampling_period = models.IntegerField()

class UrlSequence(models.Model):
    max_sequence_val = models.IntegerField(default=localsettings.URL_SEQUENCE_MAX_VAL)
    current_check_val = models.IntegerField()
    current_insert_val = models.IntegerField()

    def increase_insert_val(self):
        self.current_insert_val += 1
        self.save()

    def increase_check_val(self):
        self.current_check_val += 1
        self.save()

def get_urls_to_check():
    '''
    We need to get urls by chunks to minimize load on yandex.market/
    '''
    sequence = get_or_create_sequence()
    urls = Url.objects.filter(sampling_period=sequence.current_check_val).all()
    sequence.increase_check_val()
    return urls

def get_workers():
    '''
    We need to balance load between workers,
    as we want them to serve as long as possible.
    '''
    all_workers = Worker.objects.all()
    random.shuffle(all_workers)
    return all_workers[:len(all_workers)/10]

def get_or_create_sequence():
    sequence = UrlSequence.objects.all()
    if not len(sequence):
        sequence = UrlSequence(current_check_val = 0, current_insert_val=0)
        sequence.save()
    return sequence
