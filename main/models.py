from django.db import models
from django.contrib.auth.models import User

gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"))
navel = (("healed", "healed"), ("redish", "redish"), ("gives off smell", "gives off smell"))
height_choices = (("UP TO 150", "UP TO 150"), ("BELOW 150", "BELOW 150"))
advice = ((""))
positions = (("Doctor", "Doctor"), ("Nurse", "Nurse"), ("Pharmacist", "Pharmacist"), ("Medical Lab", "Medical Lab"),)

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
    password = models.CharField(max_length=200, blank=True, null=True)
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
    password = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.OneToOneField('Patient', null=True, blank=True, on_delete=models.CASCADE)
    appointment_with = models.ForeignKey('Doctor', null=True, blank=True, on_delete=models.CASCADE)
    appointment_date = models.DateField(blank=True)
    problem = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return f"Appointment with {self.appointment_with} on {self.appointment_date}"

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
    image = models.ImageField(upload_to='media', null=True, blank=True)
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
    child_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=gender_choices, default='MALE')
    date_of_birth = models.DateTimeField( default='2024-01-01' )
    birth_weight = models.CharField(max_length=15)
    birth_place = models.CharField(max_length=200, choices=(("Hospital", "Hospital"), ("Home", "Home"), ("Others", "Others")),  null=True, blank=True)
    baby_name = models.CharField(max_length=200, blank=True, null=True)
    father_name = models.CharField(max_length=200, blank=True, null=True)
    residence =  models.CharField(max_length=200, blank=True, null=True)
    pregnancy_number = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class PreviousPregnancyInfo(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE)
    pregnancy_number = models.IntegerField(default=1)
    number_of_births = models.IntegerField(default=1)
    living_children = models.IntegerField(default=1)
    miscarriages = models.IntegerField(default=0)
    Year_of_miscarriage = models.IntegerField(default=0)
    start_date_of_the_last_menstration = models.DateField(default='2024-01-01')
    expected_date_of_birth = models.DateField(default='2024-01-01')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class FirstTimePatientInfo(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE, null=True )
    under_20_years_old = models.BooleanField(null=True, blank=True)
    more_than_10_years_since_last_pregnancy = models.BooleanField(null=True, blank=True)
    stillbirth_infant_death_week_1 = models.BooleanField(null=True, blank=True)
    gave_birth_through_c_section = models.BooleanField(null=True, blank=True)
    had_miscarriages_2_or_more_times = models.BooleanField(null=True, blank=True)
    heart_disease = models.BooleanField(null=True, blank=True)
    tuberculosis = models.BooleanField(null=True, blank=True)
    diabetes = models.BooleanField(null=True, blank=True)
    fifth_pregnancy_or_more = models.BooleanField(null=True, blank=True)
    height_less_than_150cm = models.BooleanField(null=True, blank=True)
    hip_lameness = models.BooleanField(null=True, blank=True)
    first_pregnancy_over_35_years = models.BooleanField(null=True, blank=True)
    gave_birth_through_c_section_or_vacuum = models.BooleanField(null=True, blank=True)
    heavy_bleeding_after_child_birth = models.BooleanField(null=True, blank=True)
    placenta_stuck = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class LaboratoryMeasurement(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=200, blank=True, null=True)
    rh = models.CharField(max_length=200, blank=True, null=True)
    syphilis_sero_status = models.CharField(max_length=200, blank=True, null=True)
    other_tests = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class AttendanceReport(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE)
    attendance_date = models.DateField(default='2024-01-01')
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
    malaria =   models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
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



    # NEW MODELS      # NEW MODELS

class ChildVaccineInfo(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE, default=None, null=True)
    bcg_tuberclosis_injection_right_shoulder = models.DateField(default='2024-01-01')
    polio_mouth_droplets = models.DateField(default='2024-01-01')
    DPT_HB1_injection_left_thigh= models.DateField(default='2024-01-01')
    measles_injection_right_thigh   = models.DateField(default='2024-01-01')
    vitamin_A_mouth_droplets = models.DateField(default='2024-01-01')  
    rota = models.DateField(default='2024-01-01') 
    pmeumoccocal = models.DateField(default='2024-01-01') 


class ChildFirstAttendence(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE, default=None, null=True)
    birth_weight_below_2500grams  = models.BooleanField(null=True, blank=True)
    fourth_child_or_more = models.BooleanField(null=True, blank=True)
    twin = models.BooleanField(null=True, blank=True)
    orphan = models.BooleanField(null=True, blank=True)
    death_of_siblings_under_age_of_5 = models.BooleanField(null=True, blank=True)

class ChildMonitoringAttendance(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE, default=None, null=True)
    date = models.DateTimeField( default='2024-01-01' )
    anemia = models.BooleanField(null=True, blank=True)
    body_temperature = models.CharField(max_length=200,  null=True, blank=True)
    mothers_milk = models.BooleanField(null=True, blank=True)
    milk_substitute = models.BooleanField(null=True, blank=True)
    motor_skills_improvement = models.BooleanField(null=True, blank=True)
    white_lining_of_the_mouth = models.BooleanField(null=True, blank=True)
    eyes_weaken = models.BooleanField(null=True, blank=True)
    navel =models.CharField(max_length=200, choices=navel)
    rashes_with_pus = models.BooleanField(null=True, blank=True)
    yellowish_skin = models.BooleanField(null=True, blank=True)

 




class ChildWeight(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE)
    month_0 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_1 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_2 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_3 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_4 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_5 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_6 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_7 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_8 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_9 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_10 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_11 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_12 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_13 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_14 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_15 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_16 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_17 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_18 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_19 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_20 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_21 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_22 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_23 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_24 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_30 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_36 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_42 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_48 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_54 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    month_60 = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Child Weight for Pregnancy {self.pregnancy}"
