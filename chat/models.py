from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):

    message_body = models.CharField(max_length=2000)
    datetime = models.DateTimeField('Send Datetime')
    sender = models.ForeignKey(User, related_name="message sender", default='')
    receiver = models.ForeignKey(User, related_name="message receiver", default='')
