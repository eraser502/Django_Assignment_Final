from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title', 
            'content',
            # 여기에 author를 넣으면 글쓰는 사람이 author를 고를수 있음            
        ]