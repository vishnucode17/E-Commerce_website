from django.contrib.auth.models import User
from django import forms
class UserForm(forms.ModelForm):
    password=forms.CharField(max_length=100,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password')