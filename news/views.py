from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index_view(request):
    return render(request,'news/index.html')
    # return HttpResponse("这是新闻频道首页")