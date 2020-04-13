from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=15,default = '')
    join = models.IntegerField(default = 0)
    remark = models.CharField(max_length=500,default = '')
    class Meta:
        db_table = 'users'
