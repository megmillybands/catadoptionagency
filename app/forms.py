from django import forms
from app.models import *

class CatCreationForm(forms.ModelForm):

    class Meta:
        model = Cat
        fields = ['name', 'age', 'gender', 'breed', 'description']