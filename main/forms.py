from django import forms 

class QuestionForm(forms.Form):
    text = forms.CharField(max_length=1000)
    image = forms.ImageField(required=False, label="Image")

class SearchForm(forms.Form):
    text = forms.CharField(max_length=2000)
    

