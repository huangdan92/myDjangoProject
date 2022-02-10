from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Book


# Create your views here.
def all_book(request):
    all_book = Book.objects.all()
    return render(request, 'bookstore/all_book.html', locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        print('--update book error is %s' % (e))
        return HttpResponse('--The book is not existed')

    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())

    elif request.method == 'POST':
        price = request.POST['price']
        market_price = request.POST['market_price']

        # 改
        book.price = price
        book.market_price = market_price
        # 保存
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')
