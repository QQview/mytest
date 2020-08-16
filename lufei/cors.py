
from  django.middleware.common import CommonMiddleware
class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CORSMiddleware(MiddlewareMixin):

    def process_response(self,request,response):
        #  添加响应头
        # 运行你的域名来获取我的数据

        response["Access-Control-Allow-Origin"] ="*"
        # * 允许所有的响应
        # 允许你携带content-type请求头
        if request.method == 'OPTIONS':
            response["Access-Control-Allow-Headers"] = "Content-Type"
        #  允许你发送get。post
        response["Access-Control-Allow-Methods"] ="GET,POST,DELETE,PUT"
        return response