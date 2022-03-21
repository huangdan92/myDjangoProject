from django.utils.deprecation import MiddlewareMixin

class MyMW(MiddlewareMixin):

    def process_request(self,request):
        print('request do')


    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('view do')


    def process_response(self,request,response):
        print('response do')
        return response



class MyMW2(MiddlewareMixin):

    def process_request(self,request):
        print('request do2')


    def process_view(self,request,callback,callback_args,callback_kwargs):
        print('view do2')


    def process_response(self,request,response):
        print('response do2')
        return response