from django import forms
from app.models import *

class CatCreationForm(forms.ModelForm):

    class Meta:
        model = Cat
        fields = ['name', 'age', 'gender', 'breed', 'price', 'description', 'image']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) 
        super(CatCreationForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(CatCreationForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
    

class MessageForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=500)
