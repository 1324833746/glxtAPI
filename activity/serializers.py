from rest_framework import serializers
from .models import Activity

class ActivitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Activity #指定的模型类
        fields = ('pk','activity_name','activity_content','activity_join','activity_deadline','activity_num','activity_maxnum','activity_time','url')#需要序列化的属性
