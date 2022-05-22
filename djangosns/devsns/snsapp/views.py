from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm, CommentForm, FreeCommentForm, FreePostForm
from .models import Post, FreePost, FreeComment
from django.core.paginator import Paginator #페이지네이션

# Create your views here.
def home(request):
  # 글들의 목록들을 가져오자
  #posts = Post.objects.all()
  posts = Post.objects.filter().order_by('-date')

  # Paginator(객체, 페이지안에 몇개 보일것인지)
  paginator = Paginator(posts, 5)
  pagenum = request.GET.get('page')  # 페이지 넘버에 해당하는 숫자 /?page=pagenum
  posts = paginator.get_page(pagenum) # 페이지에 해당하는 포스트 정보들

  return render(request, 'index.html', {'posts':posts})


def postcreate(request):
  # request method가 POST일 경우 입력값 저장
  if request.method == 'POST' or request.method == "FILES":
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')

  # GET 일 경우 form 입력 html 띄우기
  else:
    form = PostForm()
  return render(request, 'post_form.html', {'form':form})


def detail(request, post_id):
  post_detail = get_object_or_404(Post, pk=post_id)
  comment_form = CommentForm()
  return render(request, 'detail.html', 
  {'post_detail':post_detail, 'comment_form':comment_form})

def new_comment(request, post_id):
  # detail.html에서 댓글을 작성 후 제출했을 때 실행됨
  # 댓글을 저장해주는 기능만 구현하면 됨
  filled_form = CommentForm(request.POST)
  if filled_form.is_valid():
    finished_form = filled_form.save(commit=False)
    # 어떤 게시물에 달려있는 댓글인지 -> Foreign Key 
    finished_form.post = get_object_or_404(Post, pk=post_id)
    finished_form.save()

  return redirect('detail', post_id)


def freehome(request):
  freeposts = FreePost.objects.filter().order_by('-date')
  # Paginator(객체, 페이지안에 몇개 보일것인지)
  paginator = Paginator(freeposts, 5)
  pagenum = request.GET.get('page')  # 페이지 넘버에 해당하는 숫자 /?page=pagenum
  freeposts = paginator.get_page(pagenum) # 페이지에 해당하는 포스트 정보들
  return render(request, 'free_index.html', {'freeposts':freeposts})

def freepostcreate(request):
  if request.method == 'POST' or request.method == 'FILES':
    form = FreePostForm(request.POST, request.FILES)
    if form.is_valid():
      unfinished = form.save(commit=False)
      unfinished.author = request.user
      unfinished.save()
      return redirect('freehome')

  else:
    form = FreePostForm()
  return render(request, 'free_post_form.html', {'form':form})

def freedetail(request, post_id):
  post_detail = get_object_or_404(FreePost, pk=post_id)
  comment_form = FreeCommentForm()
  return render(request, 'free_detail.html', 
    {'post_detail':post_detail, 'comment_form':comment_form})

def new_freecomment(request, post_id):
  filled_form = FreeCommentForm(request.POST)
  if filled_form.is_valid():
    finished_form = filled_form.save(commit=False)
    finished_form.post = get_object_or_404(FreePost, pk=post_id)
    finished_form.save()
  return redirect('freedetail', post_id)