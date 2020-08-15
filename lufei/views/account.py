from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from lufei import models
import uuid


class AuthView(APIView):

    def post(self,request, *args, **kwargs):
        """
        用户登录认证
        """
        ret = {'code': 1000}
        user = request.data.get('user')
        pwd =  request.date.get('pwd')
        user = models.Account.objects.filter(user=user, pwd=pwd).first()

        if not user :
            ret['code'] = 10001
            ret['error'] = '用户密码错误'

        else:
            uid = str(uuid.uuid4())
            models.UserToken.objects.update_or_create(user=user,defaults={'token': uid})
            ret['token'] = uid
        return Response(ret)

