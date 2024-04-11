from django import forms
from main.models import Doctor, FirstTimePatientInfo, LabaratoryMaasurement, Patient, Pregnance, PreviousPregnanciesInfo

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

        widgets = {
            'number_ya_uandikishaji': forms.TextInput(attrs={'class': 'form-control'}),
            'jina_kamili': forms.TextInput(attrs={'class': 'form-control'}),
            'umri': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'anuani': forms.TextInput(attrs={'class': 'form-control'}),
            'number_ya_simu': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'jina_la_mume': forms.TextInput(attrs={'class': 'form-control'}),
            'kimo': forms.Select(attrs={'class': 'form-select'}),
            'kazi': forms.TextInput(attrs={'class': 'form-control'}),
            'kijiji_au_mtaa': forms.TextInput(attrs={'class': 'form-control'}),
            'jina_la_mwenyekiti': forms.TextInput(attrs={'class': 'form-control'}),
            'kata_wilaya': forms.TextInput(attrs={'class': 'form-control'}),
            'elimu': forms.TextInput(attrs={'class': 'form-control'}),
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
            'cheo': forms.Select(attrs={'class': 'form-select'}),
        }


class PregnanceForm(forms.ModelForm):
    class Meta:
        model = Pregnance
        exclude = ['patient']

        widgets = {
            'jina_la_mtoto': forms.TextInput(attrs={'class': 'form-control'}),
            'mimba_ya_ngapi': forms.NumberInput(attrs={'class': 'form-control'}),
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

class PreviousPregnanciesInfoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PreviousPregnanciesInfo
        exclude = ['pregnance']

class FirstTimePatientInfoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = FirstTimePatientInfo
        exclude = ['pregnance']

class LabaratoryMaasurementForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = LabaratoryMaasurement
        exclude = ['pregnance']