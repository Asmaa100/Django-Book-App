from django import forms
from django.forms import ModelForm,widgets
from minBooks.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields=" __all__"
        fields=["name" ,"description" ,"image" ,"price","published_at","appropriate_to","author"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'published_at': forms.TextInput(attrs={'class': 'form-control'}),
            'appropriate_to': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

