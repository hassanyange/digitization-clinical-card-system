from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


# Register your models here.


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(FirstTimePatientInfo)
admin.site.register(LaboratoryMeasurement)
admin.site.register(PreviousPregnancyInfo)