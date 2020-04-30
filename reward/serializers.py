from rest_framework import serializers
from .models import Reward

class RewardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reward #指定的模型类
        fields = ('pk','reward_name','reward_content','reward_join','reward_num','url')#需要序列化的属性
