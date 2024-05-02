from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from main.form import DoctorForm
from .models import *
from .forms import *


# Create your views here.
@login_required
def home(request):
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    # total_researchers = Researcher.objects.count()
    total_users = User.objects.count()

    context = {
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_users': total_users,
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
    patients_list = Patient.objects.all()
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
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
    patient = Patient.objects.get(id=id)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect(patients)

    context = {'form': form}
    return render(request, 'edit_patient.html', context)


# delete patient
@login_required
def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect(patients)


def doctors(request):
    doctors_list = Doctor.objects.all()
    form = DoctorForm()

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor added successfully')
            return redirect(doctors)
    context = {'doctors': doctors_list, 'form': form}
    return render(request, 'doctors.html', context)


def pregnance(request, id):
    pregnancey = get_object_or_404(Pregnancy, id=id)
    first_tm, _ = FirstTimePatientInfo.objects.get_or_create(
        pregnancy=pregnancey)
    previous_tm, _ = PreviousPregnancyInfo.objects.get_or_create(
        pregnancy=pregnancey)
    labaratory_tm, _ = LaboratoryMeasurement.objects.get_or_create(
        pregnancy=pregnancey)
    first_pregnance_form = FirstTimePatientInfoForm(instance=first_tm)
    previous_pregnancies_form = PreviousPregnancyInfoForm(instance=previous_tm)
    labaratory_info_form = LaboratoryMeasurementForm(instance=labaratory_tm)

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

    context = {
        'pregnance': pregnancey,
        'first_pregnance_form': first_pregnance_form,
        'previous_pregnancies_form': previous_pregnancies_form,
        'labaratory_info_form': labaratory_info_form
    }
    return render(request, 'pregnance.html', context)



def child_data(request, id):
    
    context={}
    return render(request, 'child_data.html', context)
