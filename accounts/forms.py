from django import forms
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm

class C_UserCreationForm(UserCreationForm):
    email= forms.EmailField(
        required=False,
        widget=forms.EmailInput())
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widget={
            'username':forms.TextInput(),
            'password1':forms.PasswordInput(),
            'password2':forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email already exists. Please try another email.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

class EditUsernameForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['username']

        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
        }

  
class EditEmailForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['email']

        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

  
class C_PasswordResetForm(forms.Form):
    new_password=forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
        label='New Password'
    )
    confirm_password=forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirm Password'
    )
    
    def clean(self):
        cleaned_data = super().clean()
        new_pass = cleaned_data.get('new_password')
        confirm_pass = cleaned_data.get('confirm_password')
        
        if new_pass and confirm_pass and new_pass != confirm_pass:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data


