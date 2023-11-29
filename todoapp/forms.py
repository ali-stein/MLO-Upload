from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    assignment = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder':'Add Assignment'}))
    type = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder':'Add Type'}))
    classes = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder':'Add Class'}))
    duedate = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder':'Add Dute Date: mm/dd/yyyy'}))
    class Meta:
        model = Task 
        fields = ['assignment', 'type', 'classes', 'duedate']

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task 
        fields = '__all__'