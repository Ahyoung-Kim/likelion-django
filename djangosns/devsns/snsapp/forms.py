from dataclasses import field
from django import forms
from .models import Post, Comment

# 입력값을 받아들일 수 있는 form 작성
class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)

    self.fields['title'].widget.attrs = {
      'class': 'form-control',
      'placeholder': '글 제목을 입력해주세요',
      'rows': 20
    }
    self.fields['body'].widget.attrs = {
      'class': 'form-control',
      'placeholder': '글 본문을 입력해주세요',
      'rows': 20,
      'cols': 100
    }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment']

  def __init__(self, *args, **kwargs):
    super(CommentForm, self).__init__(*args, **kwargs)

    self.fields['comment'].widget.attrs = {
      'class': 'form-control',
      'placeholder': '댓글을 입력해주세요',
      'rows': 20
    }