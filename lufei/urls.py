from django.conf.urls import url,include

from lufei.views import course,article
from lufei.views import index

urlpatterns = [
    # 获取课程列表
    url(r'^course/$', course.CourseView.as_view({'get':'list'})),
    url(r'^course/(?P<pk>\d+)/detail', course.CourseView.as_view({'get':'retrieve'})),
    # 获取首页列表
   # url(r'/$', index.IndexView.as_view({'get':'index'}))
    # 获取文章列表
    url(r'^article/$', article.ArticleView.as_view({'get': 'list'})),
    url(r'^article/(?P<id>\d+)/detail', article.ArticleView.as_view({'get':'article_detail'}))
]
