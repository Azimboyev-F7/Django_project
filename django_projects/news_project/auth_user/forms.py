from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
