from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_jwt.authentication import jwt_decode_handler
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializers


class UserViewSet(viewsets.ModelViewSet):
        #permission_classes = (IsAuthenticated,)
    #指定结果集并设置排序
        queryset = User.objects.all().order_by('-pk')
    #指定序列化的类
        serializer_class = UserSerializers
        @action(methods=['get'], detail=False)
        def get(self, request):
            token = request.META.get('HTTP_AUTHORIZATION')[4:]
            token_user = jwt_decode_handler(token)
            print(token_user)
            if token_user:#如果验证通过
                user_id = token_user['user_id']  # 获取用户id
                print(self.request.data)
                #
                dic = {}
                get_token = self.request.query_params.get('token')
                if(get_token=='1'):
                    dic["id"] = token_user['user_id']
                mobile = self.request.query_params.get('mobile')
                if(mobile):
                    dic["mobile"]=mobile
                id = self.request.query_params.get('id')
                if (id):
                    dic["id"] = id
                username = self.request.query_params.get('username')
                if (username):
                    dic["username"] = username
                join = self.request.query_params.get('join')
                if (join):
                    dic["join"] = join
                users = User.objects.filter(**dic)

                #users = users.objects.filter(mobile=mobile)
                #users = User.objects.all()
                serializer = UserSerializers(instance=users,many=True)
                return Response(serializer.data)

            # action是drf提供的路由和视图方法绑定关系的装饰器
            # from rest_framework.decorators import action
            # 参数1: methods 列表，设置视图方法允许哪些http请求访问进来
            # 参数2: detail  当前是否方法是否属于详情页视图，
            #        False，系统不会自动增加pk在生成的路由地址中
            #        True  则系统会自动增加pk在生成的路由地址
