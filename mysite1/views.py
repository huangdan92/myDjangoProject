from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

POST_FORM = '''
<form method ='post' action = '/test_get_post/'>
    yonghuming:<input type='text' name='uname'>
    <input type = 'submit' value='提交'>
</form>
'''

def pagen_view(requst,pg):
    html = '这是编号为%s的网页'%(pg)
    return HttpResponse(html)

def cal2_view(request,x,op,y):
    html = 'x:%s op:%s y:%s' %(x,op,y)
    return HttpResponse(html)



def test_get_post(requst):
    # print()
    # html = "<h1>hello dandan</h1>"
    if requst.method == 'GET':
        print(requst.GET.getlist('a', '默认'))
        return HttpResponse(POST_FORM)
    elif requst.method == 'POST':
        print(requst.POST['uname'])
        return HttpResponse('ok')


def test_html(request):
    # from django.template import loader
    # t=loader.get_template('test_html.html')
    # html = t.render()
    # return HttpResponse(html)
    dic = {'username': 'dan', 'age': 30}
    return render(request, 'test_html.html', dic)


def test_if_for(request):
    dic = {}
    dic['x'] = 11
    return render(request, 'test_if_for.html', dic)


def test_mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')

    elif request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
        return render(request, 'mycal.html', locals())


def base_view(request):
    return render(request, 'base.html')


def music_view(request):
    return render(request, 'music.html')


def sport_view(request):
    return render(request, 'sport.html')


def test_url(request):
    return render(request, 'test_url.html')


def test_url_result(request, age):
    url = reverse('base_index')
    return HttpResponseRedirect(url)
    # return HttpResponse('ok')

def test_static(request):
    return render(request,'test_static.html')