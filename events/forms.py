from django import forms
from django.forms import ModelForm
from .models import EventLocation, Event 

# Create a location form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'event_location', 'attendees', 'description',)
        #labels = {
            #'name': forms.TextInput(attrs={'class':'form-control'}),
            #'address':forms.TextInput(attrs={'class':'form-control'}),
            #'zip_code': forms.TextInput(attrs={'class':'form-control'}),
            
        #}

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Required'}),
            'event_date':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Required' ' YYYY-MM-DD HH:MM:SS'}),
            'event_location': forms.Select(attrs={'class':'form-control', 'placeholder': 'Required'}),
            'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder': 'Required'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Required'}),
            
        }

# Create a location form 
class EventLocationForm(ModelForm):
    class Meta:
        model = EventLocation
        fields = ('name', 'address', 'zip_code',)
        #labels = {
            #'name': forms.TextInput(attrs={'class':'form-control'}),
            #'address':forms.TextInput(attrs={'class':'form-control'}),
            #'zip_code': forms.TextInput(attrs={'class':'form-control'}),
        #}

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Required'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Optional'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Optional'}),
        }
