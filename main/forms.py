from django import forms
from main.models import ChildWeight, Doctor, FirstTimePatientInfo,Appointment,ChildFirstAttendence, ChildMonitoringAttendance, ChildVaccineInfo, AttendanceReport, Researcher, LaboratoryMeasurement, Patient, Pregnancy, PreviousPregnancyInfo
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
            'patient': forms.Select(attrs={'class': 'form-select'}),
            'problem': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_with': forms.Select(attrs={'class': 'form-select'}),
            'appointment_date': forms.DateTimeInput(attrs={'class': 'form-control'}),          
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
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_place': forms.Select(attrs={'class': 'form-select'}),
            'residence': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_weight': forms.TextInput(attrs={'class': 'form-control'}),
            'pregnancy_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'child_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control'}),
            
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

class AttendanceReportForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = AttendanceReport
        exclude = ['pregnacy']


# NEW FORMS NEW FORMS 


class ChildFirstAttendenceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ChildFirstAttendence
        exclude = ['pregnancy']

class ChildVaccineInfoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ChildVaccineInfo
        exclude = ['pregnancy']

class ChildMonitoringAttendanceForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ChildMonitoringAttendance
        exclude = ['pregnacy']






class ChildWeightForm(forms.ModelForm):
    class Meta:
        model = ChildWeight
        fields = [
            'month_0', 'month_1', 'month_2', 'month_3', 'month_4', 'month_5', 
            'month_6', 'month_7', 'month_8', 'month_9', 'month_10', 'month_11', 
            'month_12', 'month_13', 'month_14', 'month_15', 'month_16', 'month_17', 
            'month_18', 'month_19', 'month_20', 'month_21', 'month_22', 'month_23', 
            'month_24', 'month_30', 'month_36', 'month_42', 'month_48', 'month_54', 
            'month_60'
        ]
        widgets = {
            'month_0': forms.NumberInput(attrs={'step': 0.1}),
            'month_1': forms.NumberInput(attrs={'step': 0.1}),
            'month_2': forms.NumberInput(attrs={'step': 0.1}),
            'month_3': forms.NumberInput(attrs={'step': 0.1}),
            'month_4': forms.NumberInput(attrs={'step': 0.1}),
            'month_5': forms.NumberInput(attrs={'step': 0.1}),
            'month_6': forms.NumberInput(attrs={'step': 0.1}),
            'month_7': forms.NumberInput(attrs={'step': 0.1}),
            'month_8': forms.NumberInput(attrs={'step': 0.1}),
            'month_9': forms.NumberInput(attrs={'step': 0.1}),
            'month_10': forms.NumberInput(attrs={'step': 0.1}),
            'month_11': forms.NumberInput(attrs={'step': 0.1}),
            'month_12': forms.NumberInput(attrs={'step': 0.1}),
            'month_13': forms.NumberInput(attrs={'step': 0.1}),
            'month_14': forms.NumberInput(attrs={'step': 0.1}),
            'month_15': forms.NumberInput(attrs={'step': 0.1}),
            'month_16': forms.NumberInput(attrs={'step': 0.1}),
            'month_17': forms.NumberInput(attrs={'step': 0.1}),
            'month_18': forms.NumberInput(attrs={'step': 0.1}),
            'month_19': forms.NumberInput(attrs={'step': 0.1}),
            'month_20': forms.NumberInput(attrs={'step': 0.1}),
            'month_21': forms.NumberInput(attrs={'step': 0.1}),
            'month_22': forms.NumberInput(attrs={'step': 0.1}),
            'month_23': forms.NumberInput(attrs={'step': 0.1}),
            'month_24': forms.NumberInput(attrs={'step': 0.1}),
            'month_30': forms.NumberInput(attrs={'step': 0.1}),
            'month_36': forms.NumberInput(attrs={'step': 0.1}),
            'month_42': forms.NumberInput(attrs={'step': 0.1}),
            'month_48': forms.NumberInput(attrs={'step': 0.1}),
            'month_54': forms.NumberInput(attrs={'step': 0.1}),
            'month_60': forms.NumberInput(attrs={'step': 0.1}),
        }
