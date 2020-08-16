from lufei import models

from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    """ 文章序列化"""
   # article_source = serializers.StringRelatedField()
    source = serializers.CharField(source='source.name')
    class Meta:
        model = models.Article
        fields = ['id', 'title','source','brief',]


class ArticleDetailSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source='source.name')

    class Meta:
        model = models.Article
        fields = ['id', 'title', 'source','brief', 'content','comment_num',
                  'agree_num', ]
