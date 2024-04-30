from django import forms
from main.models import Doctor, FirstTimePatientInfo, LaboratoryMeasurement, Patient, Pregnancy, PreviousPregnancyInfo
from django.contrib.auth.models import User

class AccountDetailsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

        widgets = {
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'husband_name': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.Select(attrs={'class': 'form-select'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control'}),
            'village_or_street': forms.TextInput(attrs={'class': 'form-control'}),
            'chairperson_name': forms.TextInput(attrs={'class': 'form-control'}),
            'ward_district': forms.TextInput(attrs={'class': 'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'position': forms.Select(attrs={'class': 'form-select'}),
        }

class PregnancyForm(forms.ModelForm):
    class Meta:
        model = Pregnancy
        exclude = ['patient']

        widgets = {
            'baby_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pregnancy_number': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class BootstrapFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-select'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

class PreviousPregnancyInfoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PreviousPregnancyInfo
        exclude = ['pregnancy']

class FirstTimePatientInfoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FirstTimePatientInfo
        exclude = ['pregnancy']

class LaboratoryMeasurementForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = LaboratoryMeasurement
        exclude = ['pregnancy']
