
from lufei import models
import uuid
from rest_framework.views import APIView
from lufei.auth.auth import LuffAuth
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.viewsets import ViewSetMixin

class AuthView(APIView):

    def post(self,request,*args,**kwargs):
        """
        用户登录认证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        ret = {'code':1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')

        user = models.Account.objects.filter(user=user,pwd=pwd).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            models.UserToken.objects.update_or_create(user=user,defaults={'token':uid})
            ret['token'] = uid
        print(ret)
        return Response(ret)