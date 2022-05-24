from urllib import response
from django.shortcuts import render
import requests
import json
from .forms import SearchForm

API_KEY = '7a5bc1a56c7210ad49751228b40e4126'

# Create your views here.
def home(request):
  if request.method == 'POST':
    # 입력된 내용을 바탕으로 search url로 get 요쳥 보내기
    # https://api.themoviedb.org/3/search/movie?api_key=<<api_key>>&language=en-US&page=1&include_adult=false
    form = SearchForm(request.POST)
    searchword = request.POST.get('search')
    if form.is_valid():
      url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={searchword}"
      response = requests.get(url)
      resdata = response.text
      obj = json.loads(resdata)
      obj = obj['results']
      return render(request, 'search.html', {'obj':obj})

  else:
    form = SearchForm()
    url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + API_KEY
    response = requests.get(url)
    resdata = response.text # json 객체
    obj = json.loads(resdata)
    obj = obj['results']
  return render(request, 'index.html', {'obj':obj, 'form':form})


def detail(request, movie_id):
  url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
  response = requests.get(url)
  resdata = response.text

  return render(request, 'detail.html', {'resdata':resdata})