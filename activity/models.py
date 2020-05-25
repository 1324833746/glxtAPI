from django.db import models

# Create your models here.
from django.db import models
class Activity(models.Model):
    activity_name = models.CharField(max_length=45)
    activity_content = models.TextField(max_length=2000)
    activity_join = models.IntegerField()
    activity_deadline = models.DateTimeField()
    activity_num = models.IntegerField()
    activity_maxnum = models.IntegerField()
    activity_time = models.DateTimeField()
    class Meta:
        db_table = 'activity'