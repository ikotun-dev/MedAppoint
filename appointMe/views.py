from django.shortcuts import render
import random #using this to generate access codes 
from .models import Patient, Appointment
# Create your views here.

#getting the model data
Patients = Patient.objects.all()

#function for generating accesscodes : 
def generate_code():
    return ''.join(random.choices('0123456789', k=10))

#index page 
def index(request):
    return render(request, "index.html")

#signin validation code 
def signin(request):
    if request.method == "POST":
        input_email = request.POST['email']
        input_password = request.POST['password']

        patient = Patients.filter(email=input_email, password=input_password)

        #conditional statement to validate patient 
        if patient:
            return render(request, "appointment.html")
        else:
            context = { 'error' :  'Invalid username of passsword please retry' }
            return render(request, "signin.html", context)
    return render(request, "signin.html")

def appointment(request):
    if request.method == "POST":
        input_name = request.POST['name']
        input_email = request.POST['email']
        input_phone = request.POST['phone']
        input_date = request.POST['date']
        input_note = request.POST['notes']
        code = generate_code()
        new_appointment =  Appointment(email=input_email, phone_no=input_phone, notes=input_note, Appointment_date=input_date, access_code=code)
        #this saves the new 
        new_appointment.save()
        context = {
            'token' : code,
            'email' : input_email,
            'appointment_date': input_date
        }

        return render(request, "token_page.html", context)

    return render(request, "appointment.html")

def signup(request):
    if request.method == "POST":
        input_name = request.POST['name']
        input_email = request.POST['email']
        input_phone = request.POST['phone']
        input_password = request.POST['password']
        
        val_patient = Patients.filter(email=input_email)
        if val_patient : 
            context = {
                'error' : 'Email exists already. '
            }
            return render(request, "signup.html", context)

        else : 
            new_patient = Patient(email=input_email, password=input_password, phone_no=input_phone)
            new_patient.save()
            context = { 
                'created' : 'User created, Login now.'
            }
            return render(request, "signin.html", context)

    return render(request, "signup.html")

def contact(request):
    return render(request, "contact.html")