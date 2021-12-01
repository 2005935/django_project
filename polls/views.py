from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect # 라다이렉트 기능 사용
from .models import Question, Choice
from django.template import loader
from django.urls import reverse # URL 처리를 위해 request 객체는 필수 인자, question_id 인자를 받음
                                # path('<int:question_id>/vote/', views.vote, name='vote')

# Create your views here.

'''웹 클라이언트가 polls 앱에 접속하면, 간단한 문장을 응답하는 예제'''
"""
# 뷰 생성, 메시지 출력
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

    # latest_question_list 객체를 Question 테이블 객체에서 pub_date 컬럼의 역순으로 정렬하여 5개의 최근 Question 객체를 가져와서 만든다.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    ##output = ', '.join([q.question_text for q in latest_question_list]) # ', '.join는 구분자를 포함한 문자열을 반환
    ##return HttpResponse(output)

    '''뷰에서 loader를 이용하여 템플릿 불러오도록 수정
    loader 함수를 이용하여 html 불러오고, 미리 만들어둔 투표 목료 context 라는 변수를 이용해 정달 -> render() 단축 함수로 대체 가능'''
    ###template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,}
    ###return HttpResponse(template.render(context, request))
    # render() 함수를 이용하여 템플릿 불러오기
    return render(request, 'polls/index.html', context)

''' 여러 가지 뷰 추가(index:투표목록, detail:투표상세, vote:투표기능, results:투표결과) '''
# 404 error : 해당 데이터가 존재하지 않을 때 발생시키는 오류
# 상세 정보를 불러올 수 있는 투표 항목이 없을 경우 404 오류 발생 -> 단축함수 get_object_or_404로 대체 가능
def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# 뷰함수 정의, question_id는 url.py에서 path('<int:question_id>/results/', views.results, name='results') 라인 실행 후 들어옴
def results(request, question_id):
    #response = HttpResponse("Your're looking at the results of question %s." % question_id)
    #return response
    question = get_object_or_404(Question, pk=question_id)
    '''render() 함수 사용, 템플릿으로 question 변수를 넘겨주는 것은 동일하지만 템플릿 파일이 다르므로, 사용자에게 보여주는 화면이 달라짐, 
       results() 뷰 함수는 최종적으로 results.html 템플릿 코드를 렌더링한 결과인 HTML 텍스트 데이터를 담은 HttpResponse 객체를 반환'''
    return  render(request, 'polls/results.html', {'question': question})

# 결과를 출력하는 result 뷰 변경, 각 답변 항목과 추표 수를 한꺼번에 보여줌
def vote(request, question_id):
    #return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        '''Chocie 테이블을 검색, 검색조건은 pk=request_id, 
           request.POST는 제출된 폼의 데이터를 담고 있는 개체로서, 파이썬 사전처럼 request.POST['choice']는 폼 데이터에서 키가 'choice'에 해당하는 값인 choice.id를 스트림으로 리턴'''
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # 폼의 POST 데이터에서 'choice'라는 키가 없으면 keyError 인셉션 발생, 검색 조건에 맞는 객체가 없으면 Choice.DoesNotExist 익셉션 발생
    except(KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form

        # 익셉션이 발생하면, render() 함수에 의해서 question과 error_message 컨텍스트 변수를 detail.html 템플릿으로 전달,
        # 그 결과 사용자에게는 에러 메시지와 함께 질문 항목 폼을 다시 보여줘서 데이터를 재입력하도록 함
        # detail.html에서 error_message 처리하는 부분과 연결됨
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else: # 다음 익셉션이 처리되지 않고 정상 처리하는 경우
        selected_choice.votes += 1 # Choice 객체의 votes 속성, 즉 선택 카운트를 +1 증가시킴
        selected_choice.save() # 변경 사항을 Choice 테이블에 저장

        # vote() 뷰 함수에서 HttpResponseRedirect 객체 반환, 리다이렉트할 타겟 URL을 인자로 받음, 타겟 URL은 reverse() 함수로 만든다.
        # HttpResponseRedirect(url) 별다른 Response를 반환하는게 아니라, 지정된 url 페이지로 refirect 할시 적용됨
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
"""

from django.views import generic

'''제너릭 뷰로 변환'''
### Generic View (class-based views)

'''generic.ListView : 특정 모델의 리스트를 출력해주는 뷰
    어떤 모델(model)에 대해 어떻게 리스트를 얻어올지 쿼리가 필요하고(queryset), 이것을 어느 템플릿(templates_name)에 어떤 파라미터명으로 전달할지(context_object_name)을 정의해야 함'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' # context_object_name : html에 전달할 파라미터명 지정

    '''Return the last five published questions.'''
    def get_queryset(self): # get_queryset() : 데이터베이스에 query할 객체를 정하는 함수, 템플릿으로넘겨줄 model 리턴
        return Question.objects.order_by('-pub_date')[:5]

'''generic.DetailView :  특정 모델의 특정 오브젝트에 대한 자세한 정보를 출력해주는 뷰
        어떤 모델(model)의 어떤 오브젝트(pk)를 어느 템플릿(template_name)에 어떤 파라미터명(context_object_name)으로 전달할지를 정의해주어야 함'''
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else: # 다음 익셉션이 처리되지 않고 정상 처리하는 경우
        selected_choice.votes += 1 # Choice 객체의 votes 속성, 즉 선택 카운트를 +1 증가시킴
        selected_choice.save() # 변경 사항을 Choice 테이블에 저장
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))