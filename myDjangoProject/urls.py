"""myDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('page/<int:pg>', views.pagen_view),
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})', views.cal2_view),
    path('test_get_post', views.test_get_post),
    # path('test_get_post/', views.test_get_post),
    path('test_html', views.test_html),
    path('test_if_for', views.test_if_for),
    path('mycal', views.test_mycal),
    path('base_index', views.base_view, name='base_index'),
    path('music_index', views.music_view),
    path('sport_index', views.sport_view),
    path('test/url', views.test_url),
    path('test_url_result/<int:age>', views.test_url_result, name='tr'),
    path('test_static', views.test_static),

    # http://127.0.0.1:8000/music/index
    path('music/', include('music.urls')),
    path('news/', include('news.urls')),
    path('bookstore/', include('bookstore.urls')),
    path('set_cookies', views.set_cookies),
    path('get_cookies', views.get_cookies),
    path('delete_cookies', views.delete_cookies),
    path('set_session', views.set_session),
    path('get_session', views.get_session),
    path('delete_session', views.delete_session)
]
