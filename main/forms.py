from django import forms
from main.models import ChildWeight, Doctor, FirstTimePatientInfo,Appointment, Researcher, LaboratoryMeasurement, Patient, Pregnancy, PreviousPregnancyInfo
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
        exclude = ['user']

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
        exclude = ['user']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'about': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'position': forms.Select(attrs={'class': 'form-select'}),
        }



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = ['user']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'problem': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_with': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_date': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
          
        }


class ResearcherForm(forms.ModelForm):
    class Meta:
        model = Researcher
        exclude = ['user']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'about': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
          
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




class ChildWeightForm(forms.ModelForm):
    class Meta:
        model = ChildWeight
        fields = ['week_1', 'week_3', 'week_6', 'week_9', 'week_12', 'week_15',
                  'week_18', 'week_21', 'week_24', 'week_27', 'week_30', 'week_33', 'week_36',
                  'week_39', 'week_42', 'week_45', 'week_48', 'week_51', 'week_54', 'week_57',
                  'week_60']
        widgets = {
            'week_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_6': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_9': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_12': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_15': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_18': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_21': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_24': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_27': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_30': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_33': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_36': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_39': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_42': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_45': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_48': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_51': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_54': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_57': forms.NumberInput(attrs={'class': 'form-control'}),
            'week_60': forms.NumberInput(attrs={'class': 'form-control'}),
        }