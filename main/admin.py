from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


# Register your models here.


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Pregnancy)
admin.site.register(FirstTimePatientInfo)
admin.site.register(LaboratoryMeasurement)
admin.site.register(PreviousPregnancyInfo)
admin.site.register(AttendanceReport)
admin.site.register(Researcher)
admin.site.register(Appointment)
admin.site.register(ChildFirstAttendence)
admin.site.register(ChildMonitoringAttendance)
admin.site.register(ChildVaccineInfo)
