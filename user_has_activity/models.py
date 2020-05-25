from django.db import models

# Create your models here.
from django.db import models
class user_has_activity(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True,related_name='activity_user')
    activity = models.ForeignKey('activity.Activity', on_delete=models.CASCADE, null=True,related_name='activity')
    finish = models.BooleanField(default=0)
    admin = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True,related_name='admin')
    finish_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'user_has_activity'

