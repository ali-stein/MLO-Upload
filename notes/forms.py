from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control my-4'}),
            'description': forms.Textarea(attrs={'class':'form-control my-4'}),
        }
        labels = {
            'description': 'Write your note here:'
        }