from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):

    def __str__(self):
        return str(self.message_id)

    message_id = models.IntegerField(max_length=100)
    message = models.CharField(max_length=2000)
    date_send = models.DateTimeField('Send Datetime')
    sender_id = models.IntegerField(max_length=5)
    sender_name = models.CharField(max_length=200)
    receiver_id = models.IntegerField(max_length=5)
    receiver_name = models.CharField(max_length=200)
