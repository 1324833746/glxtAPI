"""glxtAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from rest_framework import routers
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from django.conf import settings
from django.conf.urls.static import static
#

#定义路由
route = routers.DefaultRouter()
#注册新的路由地址(路由到某个序列化的类)
from users import views
route.register(r'users',views.UserViewSet)
from activity import views
route.register(r'activities',views.ActivityViewSet)
from reward import views
route.register(r'rewards',views.RewardViewSet)
from user_has_activity import views
route.register(r'hasac',views.HasacViewSet)
from user_has_reward import views
route.register(r'hasrd',views.HasrdViewSet)

from users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', obtain_jwt_token),
    url('api/',include(route.urls)),
    url('xg_pd/',views.put),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
