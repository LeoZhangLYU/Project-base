from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    # 这里处理模型
    return HttpResponse("Hello, world. You're at the polls index.")
