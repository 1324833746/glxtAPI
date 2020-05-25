from rest_framework import serializers
from .models import user_has_activity

class HasacSerializers(serializers.ModelSerializer):
    class Meta:
        model = user_has_activity #指定的模型类
        fields = ('pk','user','activity','finish','admin','finish_time',)#需要序列化的属性
