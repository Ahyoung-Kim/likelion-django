from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
  # POST 요청이 들어오면 로그인 처리를 해줌
  if request.method == 'POST':
    uname = request.POST['username']
    pwd = request.POST['password']

    # 데이터베이스 안에 있는 데이터인지 확인 -> auth
    # 없다면 None, 있다면 그 유저 객체
    user = auth.authenticate(request, username=uname, password=pwd)

    if user is not None:
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, 'bad_login.html')


  # GET 요청이 들어오면 login form 을 담고있는 login.html을 띄어줌
  else:
    return render(request, 'login.html')


def logout(request):
  auth.logout(request)
  return redirect('home')