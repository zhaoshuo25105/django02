from django.http import HttpResponse


def show_views(request):
    return HttpResponse("我的地一个函数")