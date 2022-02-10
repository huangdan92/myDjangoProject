from django.shortcuts import render
from django.http import HttpResponse

from .models import Book


# Create your views here.
def all_book(request):
    all_book = Book.objects.all()
    return render(request, 'bookstore/all_book.html', locals())


def update_book(requst, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        print('--update book error is %s' % (e))
        return HttpResponse('--The book is not existed')

    if requst.method == 'GET':
        return render(requst, 'bookstore/update_book', locals())

    elif requst.method == 'POST':
        pass
