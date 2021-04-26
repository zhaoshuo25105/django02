from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True,verbose_name='邮箱')
    picture = models.ImageField(upload_to='static/upload',null=True,
                                verbose_name='头像')

    def __str__(self):
        return  self.name

    class Meta:
        db_table = 'author'
        verbose_name_plural='作者'
        ordering =['-age']





class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='名称')
    address = models.CharField(max_length=50,verbose_name='地址')
    city = models.CharField(max_length=20,verbose_name='城市')
    country = models.CharField(max_length=30,verbose_name='国家')
    website = models.URLField(verbose_name='网址')

    def __str__(self):
        return self.name
    class Meta:
        db_table='publisher'
        verbose_name_plural="出版社"


class Book(models.Model):
    title = models.CharField(max_length=50,verbose_name='书名')
    publicate = models.DateField(verbose_name='出版时间')
    publisher = models.ForeignKey(Publisher,null = True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    class Meta:
        db_table='book'
        verbose_name_plural="书籍"

class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    author =models.OneToOneField(Author,verbose_name='相公')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
        verbose_name_plural='妻子'

