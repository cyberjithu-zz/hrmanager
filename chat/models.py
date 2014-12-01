from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):

    #def __str__(self):
    #        return self.name

    user = models.ForeignKey(User)
    message = models.CharField()
    date_send = models.DateTimeField('Send Datetime')
    sender_id = models.IntegerField(max_length=5)
    sender_name = models.CharField(max_length=200)
    receiver_id = models.IntegerField(max_length=5)
    receiver_name = models.CharField(max_length=200)
