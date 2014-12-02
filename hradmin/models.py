from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class HrAdminInfo(models.Model):

    def __str__(self):
        return self.user.first_name

    user = models.ForeignKey(User)
    admin_id = models.IntegerField(max_length=5)
    active_flag = models.BooleanField(default=False)
