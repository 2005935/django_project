from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView #임포트

app_name = 'bookmark' # 북마크 앱의 url에 name space 설정하도록 변경

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'), # urlpatterns 변수에 path를 하나 더 추가해 BoookmarkCreateView를 연결
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'), # path를 추가하고 BookmarkDetailView를 연결
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]