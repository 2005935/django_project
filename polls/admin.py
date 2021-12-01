'''관리자 페이지에서 [Question] 모델을 관리하려면 등록해야 함'''
#  + [Choice]
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# Question 및 Choice를 한 화면에서 변경하기
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin): # ModelAdmin 클래스를 상속받아 새로운 QuestionAdmin 클래스 정의, 그 클래스를 admin.site.register() 함수의 두 번째 인자로 등록
    # 각 필드를 분리해서 보여주기 (fieldsets에 있는 각 튜플이 첫 번째 인자가 해당 필드의 제목이 됨)
    fieldsets = [ # 필드 순서 변경 가능
        #('Question Statement', {'fields': ['question_text']}),
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), # 필드 항목 접기
    ]

    inlines = [ChoiceInline] # Choice 모델 클래스 같이 보기
    # 레코드 리스트 컬럼 지정 (list_display 속성을 추가하면, 레코드 리스트에 보여주는 컬럼 항목 지정 가능)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # list_filter 필터 : UI 화면 우측에 필터 사이드 바 추가
    search_fields = ['question_text'] # 검색박스 추가

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)