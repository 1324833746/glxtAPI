from django.contrib import admin

# Register your models here.
from users.models import User

# 注册Model类
admin.site.register(User)
