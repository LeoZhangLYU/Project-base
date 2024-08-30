from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


# Create your views here.
def index(request):
    # 这里处理模型
    blog_list = Article.objects.order_by('title')
    context = {'blog_list': blog_list}
    return render(request, 'blog.html', context)
