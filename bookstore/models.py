from django.db import models


class Book(models.Model):
    title = models.CharField(verbose_name="书名", max_length=50, default='', unique=True)
    pub = models.CharField("出版社", max_length=100, default='')
    price = models.DecimalField("价格", max_digits=7, decimal_places=2, default=0.0)
    market_price = models.DecimalField("零售价", max_digits=7, decimal_places=2, default=0.0)
    is_active = models.BooleanField("是否活跃", default=True)

    class Meta:
        db_table = "book"
        verbose_name = "图书"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s|%s|%s|%s' % (self.title, self.pub, self.price, self.market_price)


class Author(models.Model):
    name = models.CharField("姓名", max_length=11)
    age = models.ImageField("年龄", default=1)
    email = models.EmailField("邮箱", null=True)

    class Meta:
        db_table = "author"


class Husband(models.Model):
    name = models.CharField('姓名', max_length=11)


class Wife(models.Model):
    name = models.CharField('姓名', max_length=11)
    author = models.OneToOneField(Husband, on_delete=models.CASCADE)


class Publisher(models.Model):
    name = models.CharField('出版社名称', max_length=50)


class PublisherBook(models.Model):
    title = models.CharField('书名', max_length=11)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class Author1(models.Model):
    name = models.CharField('姓名', max_length=11)


class Book1(models.Model):
    title = models.CharField('书名', max_length=11)
    authors = models.ManyToManyField(Author1)
