from django import forms
from .models import QuestionComment


class QuestionForm(forms.Form):
    text = forms.CharField(max_length=1000)
    image = forms.ImageField(required=False, label="Image")
    answer = forms.ImageField(required=True, label="Answer")


class SearchForm(forms.Form):
    text = forms.CharField(max_length=2000)


class CommentForm(forms.ModelForm):
    class Meta:
        model = QuestionComment
        fields = ['body']
