from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class EmployeeInfo(models.Model):

    def __str__(self):
            return self.name

    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    employee_id = models.IntegerField(max_length=5)
    employee_email = models.EmailField()
    date_of_join = models.DateTimeField('date joined')
    addressline_1 = models.CharField(max_length=100)
    addressline_2 = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    phone_mobile = models.CharField(max_length=14)
    phone_home = models.CharField(max_length=14)
    department = models.CharField(max_length=200)
    working_on = models.CharField(max_length=200)
