from django.contrib import admin
from django.urls import path
from django.urls import re_path
from . import views

# http://127.0.0.1:8000/music/index


urlpatterns = [
    path('admin/', admin.site.urls),

    path('all_book', views.all_book),
    path('update_book/<int:book_id>', views.update_book),
    path('delete_book', views.delete_book),
    path('test_cache', views.test_cache),
    path('test_mw',views.test_mw)

]
