from django.contrib import admin
from .models import Blog, Comment

# Register your models here.

# admin 사이트에서 우리의 데이터베이스 모델들을 볼 수 있도록 등록하자 
admin.site.register(Blog)
admin.site.register(Comment)