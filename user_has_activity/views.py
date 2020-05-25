from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_jwt.authentication import jwt_decode_handler
from .models import user_has_activity
from rest_framework import viewsets
from .serializers import HasacSerializers


class HasacViewSet(viewsets.ModelViewSet):
        #permission_classes = (IsAuthenticated,)
    #指定结果集并设置排序
        queryset = user_has_activity.objects.all().order_by('-pk')
    #指定序列化的类
        serializer_class = HasacSerializers

        @action(methods=['get'], detail=False)
        def get(self, request):
            if True:#如果验证通过
                #
                dic = {}
                u_id= self.request.query_params.get('id')
                ac_id= self.request.query_params.get('activity')
                if (u_id):
                    dic["user"] = u_id
                if (ac_id):
                    dic["activity"] = ac_id
                res = user_has_activity.objects.filter(**dic)

                #users = users.objects.filter(mobile=mobile)
                #users = User.objects.all()
                serializer = HasacSerializers(instance=res,many=True)
                return Response(serializer.data)

            # action是drf提供的路由和视图方法绑定关系的装饰器
            # from rest_framework.decorators import action
            # 参数1: methods 列表，设置视图方法允许哪些http请求访问进来
            # 参数2: detail  当前是否方法是否属于详情页视图，
            #        False，系统不会自动增加pk在生成的路由地址中
            #        True  则系统会自动增加pk在生成的路由地址
