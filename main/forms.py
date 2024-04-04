from django import forms
from main.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'address', 'phone_number', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }