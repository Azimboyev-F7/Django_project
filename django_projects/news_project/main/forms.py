from django import forms

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

class LoginForm(forms.Form):
    class Meta:
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        model = Login

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'id': 'exampleInputUsername'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'id': 'exampleInputPassword'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'id': 'exampleInputFirstName'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'id': 'exampleInputLastName'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'id': 'exampleInputEmail'})
