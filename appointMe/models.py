from django.db import models

# Create your models here.
class Patient(models.Model):
    email = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=35)

    def __str__(self):
        return f"self.email"
    
    
class Appointment(models.Model):
    email = models.CharField(max_length=30, null=True, blank=True)
    phone_no = models.CharField(max_length=35)
    Appointment_date = models.DateField()
    notes = models.CharField(max_length=200)
    access_code = models.CharField(max_length=190 , default=0000)
    date_booked = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"self.access_code"
