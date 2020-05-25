from rest_framework import serializers
from .models import user_has_reward
from django.contrib.auth.models import User
class HasrdSerializers(serializers.ModelSerializer):
    class Meta:
        model = user_has_reward #指定的模型类
        fields = ('pk','user','reward','reward_time','finish','finish_time')#需要序列化的属性

