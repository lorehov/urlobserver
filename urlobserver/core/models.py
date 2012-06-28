from django.db import models

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
    url = models.CharField(max_length=1000)

class Url(models.Model):
    subscribers = models.ManyToManyField(Subscriber)
    last_updated_by = models.ForeignKey(Worker, related_name='urls')

    url = models.CharField(max_length=1000)

def get_urls_to_check():
    '''
    We need to get urls by chunks to minimize load on yandex.market/
    '''
    return Url.objects.all()

def get_workers():
    '''
    We need to balance load between workers,
    as we want them to serve as long as possible.
    '''
    return Worker.objects.all()
