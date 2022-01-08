from django import forms 

class QuestionForm(forms.Form):
    text = forms.CharField(max_length=100)
    image = forms.ImageField(required=False, label="Image")


