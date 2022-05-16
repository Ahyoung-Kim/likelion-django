from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.forms import CharField

# Create your models here.
class Blog(models.Model):
  # 데이터 마다 타입 명시해주기
  # 괄호 안에 제약사항 명시하기
  title = models.CharField(max_length=200)
  body = models.TextField()
  photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
  # auto_now_add 자동으로 지금 시간을 추가하겠다
  date = models.DateTimeField(auto_now_add=True)

  # Blog Object(1) 이라고 뜨는 것보단 제목으로 보이게 하쟝
  def __str__(self):
    return self.title

class Comment(models.Model):
  comment = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)
  # 위 두개만 추가하면 어떤 게시물에 대한 댓글인지 몰라
  # 블로그 객체 참조하도록 해야함
  # 다른 테이블을 참조 -> Foriegn Key
  # post는 Blog 객체를 참조하는 외래키인데 해당 게시물이 삭제된다면
  # 얘도 같이 삭제할께요 -> models.CASCADE
  post = models.ForeignKey(Blog, on_delete=models.CASCADE)

  def __str__(self):
    return self.comment