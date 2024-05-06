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
        fields = ['month_1', 'month_3', 'month_6', 'month_9', 'month_12', 'month_15',
                  'month_18', 'month_21', 'month_24', 'month_27', 'month_30', 'month_33', 'month_36',
                  'month_39', 'month_42', 'month_45', 'month_48', 'month_51', 'month_54', 'month_57',
                  'month_60']
        widgets = {
            'month_1': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_3': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_6': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_9': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_12': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_15': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_18': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_21': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_24': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_27': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_30': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_33': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_36': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_39': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_42': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_45': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_48': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_51': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_54': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_57': forms.NumberInput(attrs={'class': 'form-control'}),
            'month_60': forms.NumberInput(attrs={'class': 'form-control'}),
        }
