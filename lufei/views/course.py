from lufei import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet # 继承了增删改查
from lufei.serializers.course import CourseSerializer,CourseDetailSerializer
from lufei.auth.auth import LuffAuth



# apiview 给我提供接口
class CourseView(ViewSetMixin, APIView):

    def list(self,request, *args, **kwargs):
        """
        课程列表接口
        """
        ret = {'code':200,'data':None}
        try:
            querset = models.Course.objects.all()
            print(querset)
            ser = CourseSerializer(instance=querset, many=True)
            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 500
            ret['data'] = '课程获取失败'
        return Response(ret)

    def retrieve(self,request, *args, **kwargs):
        """
            课程详细接口
        """
        ret = {'code': 200, 'data': None}

        try:
            pk = kwargs.get('pk')
            print(pk)
            #课程详细对象
            obj = models.CourseDetail.objects.filter(course_id=int(pk)).first()
            print(obj)
            ser = CourseDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data

        except Exception as e:
            ret['code'] = 204
            ret['data'] = '服务器成功处理了请求，但没有返回任何数据，也许是数据不存在'

        return  Response(ret)


class MicroView(APIView):
    authentication_classes = [LuffAuth,]

    def get(self,request, *args, **kwargs):

        ret= {'code': 1000, 'title':'薇职位'}
        return Response(ret)


