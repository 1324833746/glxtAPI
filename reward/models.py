from django.db import models

# Create your models here.
from django.db import models
class Reward(models.Model):
    reward_name = models.CharField(max_length=45)
    reward_content = models.CharField(max_length=200)
    reward_join = models.IntegerField()
    reward_num = models.IntegerField()
    class Meta:
        db_table = 'reward'