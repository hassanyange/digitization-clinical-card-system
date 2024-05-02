from django.db import models
from django.contrib.auth.models import User

gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"))
height_choices = (("UP TO 150", "UP TO 150"), ("BELOW 150", "BELOW 150"))
advice = ((""))
positions = (("Doctor", "Doctor"), ("Nurse", "Nurse"), ("Pharmacist", "Pharmacist"), ("Lab Technician", "Lab Technician"),)

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True, choices=positions)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Researcher(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='patients', null=True, blank=True)
    husband_name = models.CharField(max_length=200, blank=True, null=True)
    height = models.CharField(max_length=110, null=True, choices=height_choices)
    occupation = models.CharField(max_length=200, blank=True, null=True)
    village_or_street = models.CharField(max_length=200, blank=True, null=True)
    chairperson_name = models.CharField(max_length=200, blank=True, null=True)
    ward_district = models.CharField(max_length=200, blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.full_name
    
class Pregnancy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    baby_name = models.CharField(max_length=200, blank=True, null=True)
    pregnancy_number = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class PreviousPregnancyInfo(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE)
    pregnancy_number = models.IntegerField(default=1)
    number_of_births = models.IntegerField(default=1)
    living_children = models.IntegerField(default=1)
    miscarriages = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class FirstTimePatientInfo(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE, null=True )
    under_20_years_old = models.BooleanField(null=True, blank=True)
    more_than_10_years_since_last_pregnancy = models.BooleanField(null=True, blank=True)
    gave_birth_through_c_section = models.BooleanField(null=True, blank=True)
    had_miscarriages_2_or_more_times = models.BooleanField(null=True, blank=True)
    heart_disease = models.BooleanField(null=True, blank=True)
    tuberculosis = models.BooleanField(null=True, blank=True)
    diabetes = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class LaboratoryMeasurement(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=200, blank=True, null=True)
    other_tests = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class AttendanceReport(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    weight =  models.CharField(max_length=200,  null=True, blank=True)
    blood_pressure  =  models.CharField(max_length=200,  null=True, blank=True)
    albumin_in_urine =  models.CharField(max_length=200,  null=True, blank=True)
    blood =  models.CharField(max_length=200,  null=True, blank=True)
    sugar_in_urine =  models.CharField(max_length=200,  null=True, blank=True)
    gestational_age_in_weeks =  models.CharField(max_length=200,  null=True, blank=True)
    fetal_position =  models.CharField(max_length=200,  null=True, blank=True)
    presentation_from_week_36 =  models.CharField(max_length=200,  null=True, blank=True)
    fetal_heart_rate  =  models.CharField(max_length=200,  null=True, blank=True)
    fetal_movement_after_20_weeks =  models.CharField(max_length=200, choices=(("YES", "YES"), ("NO", "NO")),  null=True, blank=True)
    edema_swelling =  models.CharField(max_length=200,  null=True, blank=True)
    ferrous_sulfate =  models.CharField(max_length=200,  null=True, blank=True)
    folic_acid =  models.CharField(max_length=200,  null=True, blank=True)
    malaria =   models.ForeignKey(Patient, on_delete=models.CASCADE)
    mebendazole = models.CharField(max_length=200,  null=True, blank=True)
    attending_doctor_name =   models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)
    attending_doctor_signature = models.CharField(max_length=200,  null=True, blank=True)
    bp_40_90_or_above = models.BooleanField(null=True)
    hb_below_60_percent = models.BooleanField(null=True)
    albumin_in_urine_positive = models.BooleanField(null=True)
    sugar_in_urine_positive = models.BooleanField(null=True)
    symptoms_of_danger = models.BooleanField(null=True)
    gestational_age_more_than_40_weeks = models.BooleanField(null=True)
    fetal_death_in_uterus = models.BooleanField(null=True)
    swelling_in_legs_or_arms = models.BooleanField(null=True)
    mother_is_having_twins = models.BooleanField(null=True)
    baby_is_too_large_or_too_small_for_its_age = models.BooleanField(null=True) 
    mother_has_been_advised_where_to_deliver = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
