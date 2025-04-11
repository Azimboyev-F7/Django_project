from django import forms
from django.contrib.auth.models import User
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'image', 'author', 'tags']
        exclude = ['author']


    def __init__(self, *args, **kwargs):        
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['tags'].widget.attrs.update({'class': 'form-control'})


class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'recipe', 'is_active', 'quaantity', 'unit']
        exclude = ['recipe']
    
    def __init__(self, args, **kwargs):
        super(IngredientCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['is_active'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['quantity'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit'].widget.attrs.update({'class': 'form-control'})
    