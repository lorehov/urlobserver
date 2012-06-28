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
    callback = models.CharField(max_length=1000)

class Url(models.Model):
    subscribers = models.ManyToManyField(Subscriber)

    url = models.CharField(max_length=1000)

class Worker(models.Model):
    url = models.CharField(max_length=1000)
