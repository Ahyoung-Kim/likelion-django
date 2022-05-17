from django.shortcuts import redirect, render
from django.contrib import auth

# Create your views here.
def login(request):
  if request.method == 'POST':
    uname = request.POST['username']
    pwd = request.POST['password']
    # 만약 이 uname과 pwd 해당하는 User 객체가 있다면 그 객체를 반환하고
    # 없다면 None
    user = auth.authenticate(request, username=uname, password=pwd)
    if user is not None:
      auth.login(request, user)
      return redirect('home')
    else:
      return render(request, 'bad_login.html')

  else:
    return render(request, 'login.html')


def logout(request):
  auth.logout(request)
  return redirect('home')