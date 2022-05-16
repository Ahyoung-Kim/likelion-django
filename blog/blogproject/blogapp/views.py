from django.shortcuts import render
from .models import Blog
from django.utils import timezone
from django.shortcuts import redirect
from .forms import BlogForm, BlogModelForm, CommentForm
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
  # 블로그 글들을 모조리 띄우는 코드 

  # Blog라는 객체를 데이터베이스에서 모조리 가져와라 
  # posts = Blog.objects.all()
  # date 내림차순으로 필터링해서 가져오라~
  posts = Blog.objects.filter().order_by('-date')
  return render(request, 'index.html', {'posts':posts})

# 블로그 글 작성 html을 보여주는 함수 
def new(request):
  return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):

  if(request.method == 'POST'):
    post = Blog()
    post.title = request.POST['title']
    post.body = request.POST['body']
    post.date = timezone.now()
    post.save()

  return redirect('home')

# django from을 이용해서 입력값을 받는 함수
# GET 요청과 (= 입력값을 받을 수 있는 html을 갖다 줘야함)
# POST 요청 (= 입력한 내용을 데이터베이스에 저장, form에서 입력한 내용을 처리)
#  둘 다 처리가 가능한 함수 
def formcreate(request):

  if(request.method == 'POST'):
    # 입력 내용을 DB에 저장
    form = BlogForm(request.POST)

    if form.is_valid():
      # 유효하다면 저장
      post = Blog()
      # 검증을 거친 깨끗한 데이터 cleand_data
      post.title = form.cleaned_data['title']
      post.body = form.cleaned_data['body']
      post.save()
      return redirect('home')

  else:
    # 입력을 받을 수 있는 html을 갖다주기 
    form = BlogForm()

  return render(request, 'form_create.html', {'form':form})


def modelformcreate(request):

  if request.method == 'POST' or request.method == "FILES":
    form = BlogModelForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')

  else:
    form = BlogModelForm()

  return render(request, 'model_form.html', {'form':form})


def detail(request, blog_id):
  # blog_id 번째 블로그 글을 데이터베이스로부터 갖고와서
  # Blog 객체 하나를 갖고 올건데 pk 값이 blog_id 인 객체를 가져와라
  blog_detail = get_object_or_404(Blog, pk=blog_id)

  comment_form = CommentForm()

  # blog_id 번째 블로그 글을 detail.html로 띄어주는 코드 
  return render(request, 'detail.html', 
  {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
  filled_form = CommentForm(request.POST)

  if filled_form.is_valid():
    # 일단은 저장하지 말고 대기해
    finished_form = filled_form.save(commit=False)
    finished_form.post = get_object_or_404(Blog, pk=blog_id)
    finished_form.save()

  return redirect('detail', blog_id)
