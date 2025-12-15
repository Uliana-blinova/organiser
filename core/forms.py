from django import forms
from .models import Event, Contact

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }