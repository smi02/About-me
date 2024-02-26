from django.shortcuts import render
from .models import Post1
from django.http import Http404

# Create your views here.
def list(request):
   Data = {'Posts': Post1.objects.all().order_by('-date')}
   return render(request, 'blog/blog.html', Data)

# def post(request, id):
#     post = Post1.objects.get(id=id)
#     return render(request, 'blog/post.html', {'post': post})

def post(request, id):
    try:
        post = Post1.objects.get(id=id)
    except Post1.DoesNotExist:
        raise Http404("Bài viết không tồn tại")
    
    return render(request, 'blog/post.html', {'post': post})
