from django import forms

from .models import New


class NewsForm(forms.ModelForm):
    class Meta:
        fields = ['title', 'content', 'image']
        model = New

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
