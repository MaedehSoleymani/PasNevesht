from django import forms
from accounts.models import CustomUser

class SignupForm (forms.ModelForm):
    class Meta:
        model= CustomUser
        fields= ('email','password')

class LoginForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields= ('email','password')

# class Reset_password_Form(forms.ModelForm):
#     class Meta:
#         model