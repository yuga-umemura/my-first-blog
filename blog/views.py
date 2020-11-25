from django.shortcuts import render,get_object_or_404
from django.utils import timezone
# モデルかポストをインポート	
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,'blog/post_list.html', {'posts':posts})
# 表示させたいのはクエリセットのデータなのでpostsを指定
# 前者の'posts'は名前、後者は値（クエリセット）
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html',{'post': post})

def post_new(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html',{'form':form})