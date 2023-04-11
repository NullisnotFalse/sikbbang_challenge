from django import forms
from .models import SignUpModel
from django.forms.widgets import PasswordInput
class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUpModel
        fields = ['username','email','password_check1','password_check2']
        labels = {'username':"아이디",'email':"email",'password_check1':"패스워드",'password_check2':"동일한 패스워드"}
        widgets = {"password_check1": PasswordInput(), "password_check2": PasswordInput()}
        help_texts = {'username': None}