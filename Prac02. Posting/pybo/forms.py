from django import forms
from pybo.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['subject', 'content']

        labels = {
            'subject': '제목',
            'content': '내용',
        }
