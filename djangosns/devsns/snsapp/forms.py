from dataclasses import field
from django import forms
from .models import Post, Comment

# 입력값을 받아들일 수 있는 form 작성
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']