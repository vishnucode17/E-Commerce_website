from .models import Product
from django import forms
from django.contrib.auth.models import User
# form to be filled by sellers
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password')

class ProductInfoForm(forms.Form):
    class Meta:
        model = Product
        fields='__all__'