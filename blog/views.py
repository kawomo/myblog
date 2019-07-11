from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    # 쿼리셋
    posts = Post.objects.all()
    # 뷰
    return render(request, 'blog/post_list.html', {'posts': posts})