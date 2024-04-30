from django.db import models


gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"))
kimo_choices = (("JUU YA 150", "JUU YA 150"), ("CHINI YA 150", "CHINI YA 150"))
ushauri = ((""))
vyeo = (("Doctor", "Doctor"), ("Nurse", "Nurse"), ("Pharmacist", "Pharmacist"), ("Lab Technician", "Lab Technician"),)


class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    about = models.CharField(max_length=200, blank=True, null=True)
    # status = models.BooleanField(default=True)
    cheo = models.CharField(max_length=200, blank=True, null=True, choices=vyeo)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

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
    kimo = models.CharField(max_length=110, null=True,  blank=True)
    kazi = models.CharField(max_length=200, blank=True, null=True)
    kijiji_au_mtaa = models.CharField(max_length=200, blank=True, null=True)
    jina_la_mwenyekiti = models.CharField(max_length=200, blank=True, null=True)
    kata_wilaya = models.CharField(max_length=200, blank=True, null=True)
    elimu = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.jina_kamili
    
    
class Pregnance(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    jina_la_mtoto = models.CharField(max_length=200, blank=True, null=True)
    mimba_ya_ngapi = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class PreviousPregnanciesInfo(models.Model):
    pregnance = models.ForeignKey(Pregnance, on_delete=models.CASCADE)
    mimba_ya_ngapi = models.IntegerField(default=1)
    amezaa_mara_ngapi  = models.IntegerField(default=1)
    watoto_walio_hai = models.IntegerField(default=1)
    mimba_zilizo_haribika = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class FirstTimePatientInfo(models.Model):
    pregnance = models.ForeignKey(Pregnance, on_delete=models.CASCADE)
    chini_ya_miaka_20 = models.BooleanField(null=True, blank=True)
    miaka_10_au_zaid_tokea_mimba_ya_mwisho = models.BooleanField(null=True, blank=True)
    kajifungua_kwa_kupasuliwa = models.BooleanField(null=True, blank=True)
    kuharibika_kwa_mimba_2_au_zaidi = models.BooleanField(null=True, blank=True)
    ugonjwa_wa_moyo  = models.BooleanField(null=True, blank=True)
    kifua_kikuu = models.BooleanField(null=True, blank=True)
    kisukari  = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class LabaratoryMaasurement(models.Model):
    pregnance = models.ForeignKey(Pregnance, on_delete=models.CASCADE)
    damu_group = models.CharField(max_length=200, blank=True, null=True)
    vipimo_vingine = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
##record ya mahudhurio
class AttendenceReport(models.Model):
    pregnance = models.ForeignKey(Pregnance, on_delete=models.CASCADE)
    tarehe_ya_mahudhurio = models.DateField()
    uzito =  models.CharField(max_length=200,  null=True, blank=True)
    blood_pressure  =  models.CharField(max_length=200,  null=True, blank=True)
    albimu_kwenye_mkojo =  models.CharField(max_length=200,  null=True, blank=True)
    damu =  models.CharField(max_length=200,  null=True, blank=True)
    sukari_kweny_mkojo =  models.CharField(max_length=200,  null=True, blank=True)
    umri_wa_mimba_wa_wiki =  models.CharField(max_length=200,  null=True, blank=True)
    kimo_cha_mimba_kwa_wiki =  models.CharField(max_length=200,  null=True, blank=True)
    mlalo_wa_mtoto =  models.CharField(max_length=200,  null=True, blank=True)
    kitangulizi_kuanzia_wiki_ya_36 =  models.CharField(max_length=200,  null=True, blank=True)
    mapigo_ya_moyo_ya_mtoto  =  models.CharField(max_length=200,  null=True, blank=True)
    mtoto_anacheza_baada_ya_wiki_20 =  models.CharField(max_length=200, choices=(("NDIO", "NDIO"), ("HAPANA", "HAPANA")),  null=True, blank=True)
    kivimba_miguu_odema =  models.CharField(max_length=200,  null=True, blank=True)
    ferrous_sulpate =  models.CharField(max_length=200,  null=True, blank=True)
    folic_acid =  models.CharField(max_length=200,  null=True, blank=True)
    malaria =   models.ForeignKey(Patient, on_delete=models.CASCADE)
    mebendazole = models.CharField(max_length=200,  null=True, blank=True)
    # mama_ameshahuriwa_kuhusu = models.CharField(max_length=200,  null=True, blank=True)
    jina_la_mhudumu =   models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)
    sahihi_ya_mhudumu = models.CharField(max_length=200,  null=True, blank=True)
    bp_40_90_au_zaidi = models.BooleanField(null=True)
    hb_chini_ya_60_per = models.BooleanField(null=True)
    albumin_kwenye_mkojo = models.BooleanField(null=True)
    sukari_kwenye_mkojo = models.BooleanField(null=True)
    mama_anazo_dalili_za_hatari = models.BooleanField(null=True)
    umri_wa_mimba_zaidi_ya_wiki_40 = models.BooleanField(null=True)
    mtoto_kufia_tumboni = models.BooleanField(null=True)
    kuvimba_miguu_au_mikono = models.BooleanField(null=True)
    mama_ana_mapacha = models.BooleanField(null=True)
    kipimo_cha_mimba_kikubwa_au_kidogo_kuliko_umri_wake = models.BooleanField(null=True) 
    mama_ameshauriwa_azalie_wapi  = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
     
    
    
    
    
    
    
    


 
    
    
    
    
    

