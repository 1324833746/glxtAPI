from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User #指定的模型类
        fields = ('pk','last_login','is_superuser','username','first_name','last_name','email','join','remark','mobile','password')#需要序列化的属性


