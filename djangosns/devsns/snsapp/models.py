from tkinter import CASCADE
from turtle import title
from django.db import models
from django.conf import settings

# Create your models here.

# 게시물 모델
class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title


# 댓글 모델
class Comment(models.Model):
  comment = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  # Forien Key
  post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

  def __str__(self):
      return self.comment