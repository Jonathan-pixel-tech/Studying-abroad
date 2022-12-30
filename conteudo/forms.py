from django import forms
from .models import Universidade, CollegeList

class criaUniversidade(forms.ModelForm):
    class Meta:
        model= Universidade
        exclude=()

class criaCollegeList(forms.ModelForm):
    class Meta:
        model = CollegeList
        exclude=('usuario',)
    