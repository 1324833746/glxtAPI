from django.db import models

# Create your models here.
from django.db import models
class user_has_reward(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True,related_name='reweard_user')
    reward = models.ForeignKey('reward.Reward', on_delete=models.CASCADE, null=True,related_name='reward')
    reward_time = models.DateTimeField(auto_now_add=True)
    finish = models.BooleanField(default=0)
    finish_time = models.DateTimeField()
    class Meta:
        db_table = 'user_has_reward'