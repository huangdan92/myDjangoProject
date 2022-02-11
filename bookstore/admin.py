from django.contrib import admin
from .models import Book
from .models import Author


# Register your models here.
# admin.site.register(Book)


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'market_price']
    list_display_links = ['title']
    list_filter = ['pub']
    search_fields = ['title']
    list_editable = ['price']


class AuthorManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'age']
    list_display_links = ['name']
    list_filter = ['name']
    search_fields = ['name']
    list_editable = ['age']


admin.site.register(Book, BookManager)
admin.site.register(Author, AuthorManager)
