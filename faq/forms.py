from django import forms
from .models import Question,Answer,Reply

class Question(forms.ModelForm):
    class Meta:
        model   = Question
        fields  = ["title","content","accept_dt","user"]


