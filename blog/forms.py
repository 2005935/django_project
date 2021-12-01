from django import forms
from .models import Post

class PostForm(forms.ModelForm): # ModelForm : Django에서 제공하는 model form

    class Meta:# -> class Meta : 이 폼을 만들기 위해서 어떤 model이 쓰여야하는지 장고에서 알려주는 구문
        model = Post
        fields = ('title', 'text',) # 폼에 보여질 양식(title, text)
