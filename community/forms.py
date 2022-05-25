from django import forms
from .models import Review, ReviewComment


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': '글 제목을 입력해주세요.',
            }),
            
            'movie_title' : forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                'placeholder': '영화 제목을 입력해주세요.',
            }),
            
            'rank' : forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px',
                'placeholder': '평점을 입력해주세요.',
            }),
            
            'content' : forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 400px',
                'placeholder': '내용을 입력해주세요.',
            })
        }


class ReviewCommentForm(forms.ModelForm):

    class Meta:
        model = ReviewComment
        exclude = ['review', 'user']
        widgets = {
            'content' : forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-height: 50px; max-width: 400px;',
                'placeholder': '내용을 입력해주세요.',
            })
        }