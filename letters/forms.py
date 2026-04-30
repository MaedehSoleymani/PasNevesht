from django import forms
from .models import Letter,Contact
from django.utils import timezone

class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields=['name','email']

        widgets={
            'name':forms.TextInput(),
            'email':forms.EmailInput()
        }

class LetterForm(forms.ModelForm):
    class Meta:
        model= Letter
        fields= ['receiver', 'subject', 'message','scheduled_date']

        widgets={
            'receiver':forms.EmailInput(),
            'subject':forms.TextInput(),
            'message':forms.Textarea(),
            'scheduled_date':forms.DateTimeInput(
                attrs={'type': 'datetime-local'})
        }

    def clean_scheduled_date(self):
        scheduled_date = self.cleaned_data.get('scheduled_date')
        if scheduled_date and scheduled_date < timezone.now():
            raise forms.ValidationError('You cannot schedule a message in the past. Please select a future date and time.')
        return scheduled_date