from django import forms
from .models import Page
from django.core.exceptions import ValidationError


class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Título'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Orden'}),
        }
        labels = {
            'title': '', 'content':'', 'order':''
        }