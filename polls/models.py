'''
설문조사 앱 구현하기
'''
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

'''Question, Choice 테이블 정의'''
'''Question 클래스 : __str__() 및 was_published_recently() 함수 추가, 
Choice 클래스 : __str__() 함수 추가'''

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    '''was_published_rencently 출력 모양 변경
            admin_order_field : 정렬 기준 항목, 
            boolean : 값이 Boolean 형태인지 설정하고, True이면 값 대신 아이콘으로 표시
            short_description : 항목의 헤더 이름 설정'''
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text