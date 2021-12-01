from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model): # models.Model을 상속받는 Bookmark 클래스 생성
    # 모델 안에 필드라 부르는 두 개의 클래스 변수 존재,
        # site_name, url 데이터베이스에 이 두가지의 정보를 저장하고자 함, 이 정보가 기록되는 테이블 이름은 bookmark임.
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    # get_absolute_url 메서드는 장고에서 사용하는 메서드, 보통 객체의 상세 화면 주소를 반환
        # 웹 사이트의 개별적인 모델 레코드들을 보여주기 위한 URL을 반환하는 메서드. 이 메소드가 추가되면, 관리자 사이트 안의 모델 레코드 수정화면에 View on site 버튼이 자동으로 추가됨
        # reverse() 함수는 모델의 개별적인 레코드들에 알맞은 포맷의 URL을 생성하는 역할
    def get_absolute_url(self):
        return reverse('bookmark:detail', args=[str(self.id)]) # reverse 메서드는 URL 패턴의 이름과 추가 인자를 전달받아 URL을 생성하는 메서드임