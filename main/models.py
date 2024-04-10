from django.db import models


gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"))
kimo_choices = (("JUU YA 150", "JUU YA 150"), ("CHINI YA 150", "CHINI YA 150"))

# Create your models here.
class Patient(models.Model):
    number_ya_uandikishaji = models.CharField(max_length=15)
    jina_kamili = models.CharField(max_length=50)
    umri = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    anuani = models.CharField(max_length=100)
    number_ya_simu = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='patients', null=True, blank=True)
    jina_la_mume =   models.CharField(max_length=200, blank=True, null=True)
    kimo = models.CharField(max_length=10, choices=kimo_choices)
    kazi = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class PreviousPregnanciesInfo(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    mimba_ya_ngapi = models.IntegerField(default=1)
    amezaa_mara_ngapi  = models.IntegerField(default=1)
    watoto_walio_hai = models.IntegerField(default=1)
    mimba_zilizo_haribika = models.IntegerField(default=0)
    
class FirstTimePatientInfo(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    chini_ya_miaka_20 = models.BooleanField()
    miaka_10_au_zaid_tokea_mimba_ya_mwisho = models.BooleanField()
    kajifungua_kwa_kupasuliwa = models.BooleanField()
    kuharibika_kwa_mimba_2_au_zaidi = models.BooleanField()
    ugonjwa_wa_moyo  = models.BooleanField()
    kifua_kikuu = models.BooleanField()
    kisukari  = models.BooleanField()
    
    
    
    
    
    


 
    
    
    
    
    

