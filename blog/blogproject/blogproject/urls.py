from django.conf import settings
from django.contrib import admin
from django.urls import path
from blogapp import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # html form을 이용해 블로그 객체 만들기
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # django form을 이용해 블로그 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),

    # django modelform 을 이요해 블로그 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),

    # 127.0.0.1:8000/detail/1
    # 127.0.0.1:8000/detail/2
    # 127.0.0.1:8000/detail/3
    # 127.0.0.1:8000/detail/id
    # detail/ 과 정수형태인blog_id를 detail() 함수에 인자로 넘겨줄거야
    path('detail/<int:blog_id>', views.detail, name='detail'),

    # comment url 
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
]

# media 파일을 접근할 수 있는 url도 추가해야 함 (외우는 것이 좋음)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)