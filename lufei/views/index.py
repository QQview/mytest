from lufei import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet # 继承了增删改查
from lufei.serializers.course import CourseSerializer,CourseDetailSerializer
from lufei.auth.auth import LuffAuth


class IndexView(ViewSetMixin, APIView):

    def index(self,request, *args, **kwargs):
        """首页展示列表
        """
        ret = {'code':200,'data':None}
        # try:
        #     queryset = models.Course.objects.all()
        #     ser = C
        return Response(ret)
