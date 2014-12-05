from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):

    def __str__(self):
        return str(self.message_id)

    message_id = models.IntegerField(max_length=100)
    message_body = models.CharField(max_length=2000)
    date_send = models.DateTimeField('Send Datetime')
    sender = models.ForeignKey(User, related_name="message sender", default='')
    receiver = models.ForeignKey(User, related_name="message receiver", default='')
