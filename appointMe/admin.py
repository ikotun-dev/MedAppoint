from django.contrib import admin
from .models import Patient, Appointment

admin.site.site_header = "AppointMe Doctor Dashboard"
admin.site.site_title = "Doctor"
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_no')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date_booked', 'Appointment_date', 'access_code')
    search_fields = ('access_code',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)



