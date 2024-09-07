from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def search(request):
    return HttpResponse("测试返回数据")