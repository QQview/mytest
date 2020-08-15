from lufei import models

from rest_framework import serializers


class CourseSerializer(serializers.ModelSerializer):
    """
    课程序列化
    """
    level = serializers.CharField(source='get_level_display')
    course_level = serializers.CharField(source='get_course_type_display')
    status_level = serializers.CharField(source='get_status_display')

    class Meta:
        # fields = '__all__': 表示所有字段
        # exclude = ('add_time',): 除去指定的某些字段
        model = models.Course
        fields = ['id','name','course_img','level','course_level','status_level']


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    课程详细序列化
    """
    # one2one/fk/choice
    name = serializers.CharField(source='course.name')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')# 获得选择等级
    status_level = serializers.CharField(source='course.get_status_display')

    # m2m
    # 外键关联SerializerMethodField。
    recommends = serializers.SerializerMethodField()
    # 反向查询 related_name='outlines')
    outlines = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.CourseDetail
        fields = ['course', 'video_brief_link', 'why_study','name',
                  'img', 'level', 'status_level','recommends','outlines' ]
    #
    def get_recommends(self,obj):
        # 获取推荐的所有课程
        queryset = obj.recommend_courses.all()

        return [{'id':row.id,'title':row.name,} for row in queryset]



