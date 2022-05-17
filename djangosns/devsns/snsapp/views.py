from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post

# Create your views here.
def home(request):
  # 글들의 목록들을 가져오자
  #posts = Post.objects.all()
  posts = Post.objects.filter().order_by('-date')
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