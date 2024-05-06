from decimal import Decimal
import json
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core import serializers

from main.form import DoctorForm
from .models import *
from .forms import *


# Create your views here.
@login_required
def home(request):

    user = request.user
    print(user)
    try:
        patient = Patient.objects.get(user=user)
        print("patient foundddddd")
        return redirect('patients')
    except Patient.DoesNotExist:
        print("Patient dont exist")
        pass

    total_appointments = Appointment.objects.count()
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    # total_researchers = Researcher.objects.count()
    total_users = User.objects.count()
    total_researchers = Researcher.objects.count()
    totol_childs = Pregnancy.objects.count()

    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_users': total_users,
        'total_researchers': total_researchers,
        'totol_childs': totol_childs,
        'total_appointments': total_appointments,
    }

    return render(request, 'index.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.error(request, 'Invalid credentials')
            return redirect(signin)

    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user already exists
        user = User.objects.filter(username=username).exists()
        if user:
            messages.info(request, 'User already exists')
            return render(request, 'signup.html')
        else:
            user = User.objects.create_user(
                username=username, password=password)
            user.save()
            messages.info(request, 'User created successful')
            return redirect(home)
    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    messages.info(request, "Successful logged out")
    return redirect(home)


def profile(request):
    if request.method == 'POST':
        form = AccountDetailsForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = AccountDetailsForm(instance=request.user)
    return render(request, 'accountdetails.html', {'form': form})


# list all pattients
@login_required()
def patients(request):

    try:
        if request.user.patient:
            patients_list = Patient.objects.filter(user=request.user)
            form = PatientForm()
            context = {'patients': patients_list, 'form': form}
            return render(request, 'patients.html', context)
    except:
        pass

    patients_list = Patient.objects.all()
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        username = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists')
            return redirect(patients)

        if form.is_valid():
            user = User.objects.create_user(
                username=username, email=username, password=password)
            user.save()
            data = form.save(commit=False)
            data.user = user
            data.save()
            messages.success(request, 'Patient added successfully')
            return redirect(patients)
    context = {'patients': patients_list, 'form': form}
    return render(request, 'patients.html', context)


# show one patient
@login_required
def patient(request, id):
    patienty = Patient.objects.get(id=id)
    pregnance_form = PregnancyForm()
    if request.method == 'POST':
        pregnance_form = PregnancyForm(request.POST)
        if pregnance_form.is_valid():
            pregnance = pregnance_form.save(commit=False)
            pregnance.patient = patienty
            pregnance.save()
            messages.success(request, 'Pregnance added successfully')
            return redirect(patient, id)
        else:
            messages.error(request, 'Pregnance not added')
            return redirect(patient, id)

    context = {'patient': patienty, 'pregnance_form': pregnance_form}
    return render(request, 'patient.html', context)

# register new_patient


@login_required
def new_patient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(patients)

    context = {'form': form}
    return render(request, 'new_patient.html', context)


# edit patient
@login_required
def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient', id=patient.id)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'edit_patient.html', {'form': form})


@login_required
def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients')
    return render(request, 'delete_patient.html', {'patient': patient})


def doctors(request):
    doctors_list = Doctor.objects.all()
    form = DoctorForm()

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            username = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                return redirect(doctors)
            user = User.objects.create_user(
                username=username, email=username, password=password)
            user.save()
            data = form.save(commit=False)
            data.user = user
            data.save()
            messages.success(request, 'Doctor added successfully')
            return redirect(doctors)
    context = {'doctors': doctors_list, 'form': form}
    return render(request, 'doctors.html', context)


def doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, 'doctor.html', {'doctor': doctor})


def edit_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor', id=doctor.id)
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'edit_doctor.html', {'form': form})


def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors')
    return render(request, 'delete_doctor.html', {'doctor': doctor})


def researchers(request):
    researchers_list = Researcher.objects.all()
    print(researchers_list)
    form = ResearcherForm()

    if request.method == 'POST':
        form = ResearcherForm(request.POST)
        if form.is_valid():
            username = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                return redirect(doctors)
            user = User.objects.create_user(
                username=username, email=username, password=password)
            user.save()
            data = form.save(commit=False)
            data.user = user
            data.save()
            messages.success(request, 'Researcher added successfully')
            return redirect(researchers)
    context = {'researchers': researchers_list, 'form': form}
    return render(request, 'researchers.html', context)


def researcher(request, id):
    researcher = get_object_or_404(Researcher, id=id)
    return render(request, 'researcher.html', {'researcher': researcher})


def edit_researcher(request, id):
    researcher = get_object_or_404(Researcher, id=id)
    if request.method == 'POST':
        form = ResearcherForm(request.POST, instance=researcher)
        if form.is_valid():
            form.save()
            return redirect('researcher', id=researcher.id)
    else:
        form = ResearcherForm(instance=researcher)
    return render(request, 'edit_researcher.html', {'form': form})


def delete_researcher(request, id):
    researcher = get_object_or_404(Researcher, id=id)
    if request.method == 'POST':
        researcher.delete()
        return redirect('researchers')
    return render(request, 'delete_researcher.html', {'researcher': researcher})


def appointments(request):
    appointments_list = Appointment.objects.all()
    print(appointments_list)
    form = AppointmentForm()

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            username = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'User already exists')
                return redirect(appoints)
            user = User.objects.create_user(
                username=username, email=username, password=password)
            user.save()
            data = form.save(commit=False)
            data.user = user
            data.save()
            messages.success(request, 'Appointment added successfully')
            return redirect(researchers)
    context = {'appointments': appointments_list, 'form': form}
    return render(request, 'appointments.html', context)



def appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    return render(request, 'appointment.html', {'appointment': appointment})

def edit_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    form = AppointmentForm(request.POST or None, instance=appointment)
    if form.is_valid():
        form.save()
        return redirect('appointment', id=id)
    return render(request, 'edit_appointment.html', {'form': form})

def delete_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments')
    return render(request, 'delete_appointment.html', {'appointment': appointment})




def pregnance(request, id):
    pregnancey = get_object_or_404(Pregnancy, id=id)
    first_tm, _ = FirstTimePatientInfo.objects.get_or_create(
        pregnancy=pregnancey)
    previous_tm, _ = PreviousPregnancyInfo.objects.get_or_create(
        pregnancy=pregnancey)
    labaratory_tm, _ = LaboratoryMeasurement.objects.get_or_create(
        pregnancy=pregnancey)
    attendance_tm, _ = AttendanceReport.objects.get_or_create(
        pregnancy=pregnancey)    
    first_pregnance_form = FirstTimePatientInfoForm(instance=first_tm)
    previous_pregnancies_form = PreviousPregnancyInfoForm(instance=previous_tm)
    labaratory_info_form = LaboratoryMeasurementForm(instance=labaratory_tm)
    attendance_report_form = AttendanceReportForm(instance=attendance_tm)

    if request.method == "POST" and 'first_pregnancy_form_save' in request.POST:
        first_pregnance_form = FirstTimePatientInfoForm(
            request.POST, instance=first_tm)
        print("Hello.....................................................hello")
        if first_pregnance_form.is_valid():
            first_pregnance_form.save()
            messages.success(
                request, 'First time patient info saved successfully')
            return redirect(pregnance, id)

    if request.method == "POST" and 'previous_pregnancies_form_save' in request.POST:
        previous_pregnancies_form = PreviousPregnancyInfoForm(
            request.POST, instance=previous_tm)
        if previous_pregnancies_form.is_valid():
            previous_pregnancies_form.save()
            messages.success(
                request, 'Previous pregnancies info saved successfully')
            return redirect(pregnance, id)

    if request.method == "POST" and 'labaratory_info_form_save' in request.POST:
        labaratory_info_form = LaboratoryMeasurementForm(
            request.POST, instance=labaratory_tm)
        if labaratory_info_form.is_valid():
            labaratory_info_form.save()
            messages.success(request, 'Labaratory info saved successfully')
            return redirect(pregnance, id)
    
    
    if request.method == "POST" and 'attendance_report_form_save' in request.POST:
        attendance_report_form = AttendanceReportForm(
            request.POST, instance=attendance_tm)
        if attendance_report_form.is_valid():
            attendance_report_form.save()
            messages.success(request, 'Attendance saved successfully')
            return redirect(pregnance, id)

    context = {
        'pregnancey': pregnancey,
        'first_pregnance_form': first_pregnance_form,
        'previous_pregnancies_form': previous_pregnancies_form,
        'labaratory_info_form': labaratory_info_form,
        'attendance_report_form': attendance_report_form
    }
    return render(request, 'pregnance.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Pregnancy, ChildWeight
from .forms import ChildWeightForm
from django.contrib import messages
import json

def child_data(request, id):
    pregnancy = get_object_or_404(Pregnancy, id=id)
    child_weight, created = ChildWeight.objects.get_or_create(pregnancy=pregnancy)
    
    # Get child weight data for the current pregnancy
    child_weight_data = ChildWeight.objects.filter(id=child_weight.id).values().first()

    # Transform month keys to age and weight format
    transformed_data = []
    for key, value in child_weight_data.items():
        if key.startswith('month_'):
            month_number = int(key.split('_')[1])
            age = month_number
            weight = float(value) if value is not None else None
            transformed_data.append({'age': age, 'weight': weight})

    # Convert the queryset to JSON
    json_data = json.dumps(list(transformed_data))

    form = ChildWeightForm(instance=child_weight)

    if request.method == "POST" and 'child_weight_form_save' in request.POST:
        form = ChildWeightForm(request.POST, instance=child_weight)
        if form.is_valid():
            form.save()
            messages.success(request, 'Child weight saved successfully')
            return redirect('child-data', id=id)

    context = {"weighs": child_weight, "pregnancy": pregnancy, 'form': form, 'weight_data_json': json_data}
    return render(request, 'child_data.html', context)