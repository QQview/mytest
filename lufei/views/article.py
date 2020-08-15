from lufei import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from rest_framework.viewsets import ModelViewSet # 继承了增删改查
from lufei.serializers.course import CourseSerializer,CourseDetailSerializer
from lufei.auth.auth import LuffAuth
from lufeicity.settings import ret
from lufei.serializers.article import ArticleSerializer,ArticleDetailSerializer
class ArticleView(ViewSetMixin, APIView):

    def list(self,request , *args, **kwargs):
       '''
        文章列表接口
       '''
       try:
           querset = models.Article.objects.all()
           print(querset)
           ser = ArticleSerializer(instance=querset, many=True)
           ret['data'] = ser.data
       except Exception as e:
           ret['code'] = 500
           ret['data'] = '文章获取失败'

       return Response(ret)

    def article_detail(self,request, *args, **kwargs):
        try:
            id = kwargs.get('id')
            querset = models.Article.objects.filter(id=id).first()
            print(querset)
            ser = ArticleDetailSerializer(instance=querset, many=False)
            print(ser)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 204
            ret['data'] = '服务器成功处理了请求，但没有返回任何数据，也许是数据不存在'

        return Response(ret)
