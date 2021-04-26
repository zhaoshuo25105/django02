from django.db.models import Count ,Sum
from django.http import HttpResponse, request
from django.shortcuts import render
from .models import *
from .forms import *
from .task import *
# Create your views here.


def test_views(request):
    return  HttpResponse("测试试图首页")

def tmp_views(request):
    return render(request,'01-tmp.html')

def var_views(request):
    dic = {
        'name':'jeck',
        "age":17
    }

    return render(request,'02-tmp.html',locals())

def add_views(request):
    # Author.objects.create(name='老舍',age=85,email='laoshe@163.com')
    # author = Author(name="巴金",age=75,email="bajin@163.com")
    # author.save()
    # dic ={
    #     'name':'冰心',
    #     'age':95,
    #     'email':'bingxin@163.com'
    # }
    # obj = Author(**dic)
    # obj.save()

    # book = Book(title = '红楼梦',publicate='1992-5-23')
    # book.save()
    # Book.objects.create(title='水浒传',publicate='1994-7-15')
    # Book.objects.create(title = '西游记', publicate='2018-1-13')

    publisher = Publisher(name='新华出版社',address='北京昌平区',city='北京',country='中国',website="http://www.baidu.com")
    publisher.save()
    Publisher.objects.create(name='黄埔出版社',address='上海黄浦区',city='上海',country='中国',website='http://www.jingdong.com')
    Publisher.objects.create(name='辽宁出版社',address='辽宁沈阳',city='沈阳',country='中国',website='heep://www.shenyang.com')
    return HttpResponse('add ok')

def query_views(request):
    # authors = Author.objects.filter(name__contains='巴金').values('age')
    # authors = Author.objects.filter(
    #     age__gt= Author.objects.filter(name__contains='巴金').values('age')).values("name")

    num = Author.objects.values('email').annotate(lit=Count('age')).all()
    # count = Author.objects.values('email').aggregate(avg = Count("age"))
    print(num)
    # print(authors)
    return HttpResponse('query ok')


def authors_views(request):
    authors = Author.objects.all()
    return render(request,'06-authors.html',locals())


def wife_views(request):
    # wife = Wife()
    # wife.name = '巴金夫人'
    # wife.age = 66
    # wife.author_id = 2
    # wife.save()

    # wife = Wife()
    # wife.name = '武松夫人'
    # wife.age = 45
    # author = Author.objects.get(id=4)
    # print(author)
    # wife.author = author
    # wife.save()

    # 查询
    wife = Wife.objects.get(id=1)
    wife_author = wife.author
    print('author',wife_author)

    author = Author.objects.get(id=1)
    author_wife = author.wife
    print('wife',author_wife)
    return HttpResponse('ok')


def mtm_views(request):
    # 正向查询
    book = Book.objects.get(id=1)
    authors = book.authors.all()
    return render(request,'08-mtm.html',locals())


def request_views(request):
    # a = request.META
    a = request.META['PATH_INFO']
    print(a)
    return HttpResponse('ok')


def form_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request,'04-form.html',locals())

    else:
        # subject = request.POST['subject']
        # email  = request.POST['email']
        # print(subject,email)

        form = RemarkForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data
            print(a)
        return HttpResponse('post ok')

def cookie_views(request):
    # resp = HttpResponse('添加成功')

    resp = render(request,'10-setcookie.html')
    resp.set_cookie('uname','laowang1',60*60)
    return resp

def session_views(request):
    request.session['uname1']= 'laoli'
    return HttpResponse('session ok')


# 异步任务

def celeryTest(request):

    # show()
    show.delay()
    return HttpResponse("celery ok")

