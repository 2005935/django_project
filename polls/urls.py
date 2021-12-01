'''
polls/views.py에서 생성한 뷰를 호출하기 위한 URL파일 생성
'''

from django.urls import path
from .import views

# path 함수는 path(route, view, kwargs, name) 형태로 호출
# route : 주소
# view : route의 주소로 접근했을 때 호출할 view
# kwargs : 뷰에 전달할 값들
# name : route의 이름, 원하는 곳에서 주소를 호출해 출력하거나 사용 가능

app_name = 'polls' # URL 네임스페이스 설정

''' ## Function-based view
urlpatterns=[
    path('', views.index, name='index'), # ex: /polls/
    
    #path converter : <>는 변수 의미, 해당 값을 뷰에 인자로 전달
    path('<int:question_id>/', views.detail, name='detail'), # ex: /polls/5/
    path('<int:question_id>/results/', views.results, name='results'), # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # ex:/polls/5/vote/
]'''

### Generic view(class-based view)
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'), # as_view() : 진입 메소드
    path('<int:pk>/', views.DetailView.as_view(), name='detail'), # ex: /polls/5/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'), # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'), # ex:/polls/5/vote/
]