from django.views.generic.list import ListView
from .models import Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView # UpdateView 임포트, DeleteView
from django.urls import reverse_lazy

from django.views.generic.detail import DetailView

# Create your views here.
# ListView를 상속받은 BookmarkListView 클래스형 뷰 생성
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6 # 한 페이지에 몇 개의 리스트 출력할 지 결정

class BookmarkCreateView(CreateView): # 제네릭 뷰인 CreateView를 상속받아 생성
    model = Bookmark # model : 어떤 모델의 입력을 받을 지 설정
    fields = ['site_name', 'url'] # fields : 어떤 필드들을 입력받을 지 설정하는 부분
    success_url = reverse_lazy('bookmark:list') # success_url : 북마크 추가를 완료하고 목록페이지로 이동
    template_name_suffix = '_create' # templates_name_suffix : 사용할 템플릿의 접미사만 변경하는 설정 값
    
class BookmarkDetailView(DetailView): # 제네릭 뷰인 DetailView를 상속받음
    model = Bookmark

class BookmarkUpdateView(UpdateView): # UpdateView를 상속받아 BookmarkUpdateview 생성
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update' # 템플릿 접미사를 _update로 설정하여, bookmark_update.html과 연결

class BookmarkDeleteView(DeleteView): # DeleteView를 상속받아, BookmarkDeleteView 생성
    model = Bookmark
    success_url = reverse_lazy('bookmark:list') # 목록 페이지로 가도록 reverse_lazy를 사용해 설정