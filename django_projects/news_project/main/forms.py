from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import New, Login


class NewsForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'content', 'image']
        model = New

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

class LoginForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'exampleInputPassword'}))
    class Meta:
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        model = Login

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'exampleInputUsername'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'id': 'exampleInputFirstName'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'id': 'exampleInputLastName'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id': 'exampleInputEmail'})



class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'Enter your Username',
            'id': 'exampleFormControlUsername',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'name': 'password1',
            'placeholder': 'Enter your Password',
            'id': 'exampleFormControlPassword',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'name': 'confirm_password',
            'placeholder': 'Confirm your Password',
            'id': 'exampleFormControlConfirmPassword',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'name': 'email',
            'placeholder': 'Enter your Email',
            'id': 'exampleFormControlEmail',
        })
