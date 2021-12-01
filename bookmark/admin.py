'''관리자 페이지에 모델 등록'''

from django.contrib import admin
from .models import Bookmark # 현재 폴더에 있는 models.py 파일에서 Bookmark라는 모델을 불러오겠다는 의미

# Register your models here.
admin.site.register(Bookmark)