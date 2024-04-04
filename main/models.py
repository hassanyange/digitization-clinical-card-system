from django.db import models


gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"))

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choices)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    image = models.ImageField(upload_to='patients', null=True, blank=True)

    def __str__(self):
        return self.name
    

