from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, Group
from django import forms
# from accounts.models import *


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    user_type = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select groups to join"
    )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "user_type", "username"]


class LoginForm(AuthenticationForm):
    pass
