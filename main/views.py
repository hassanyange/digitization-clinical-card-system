from decimal import Decimal
import json
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from .models import *
from .forms import ChildWeightForm
import json


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
        return redirect(patients)
    except Patient.DoesNotExist:
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
        username_or_email = request.POST["username"]
        password = request.POST["password"]

        if '@' in username_or_email:
            try:
                username = User.objects.get(email=username_or_email).username
            except User.DoesNotExist:
                messages.warning(request, 'Invalid credentials!')
                return redirect(signin)
        else:
            username = username_or_email

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.warning(request, 'Invalid credentials!')
            return redirect(signin)
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['confirm-password']
        agree_terms = request.POST.get('agree_terms', False)

        if not agree_terms:
            messages.info(request, 'You must agree to the terms and conditions!')
            return render(request, 'signup.html')

        if password != confirm_pass:
            messages.info(request, 'Password not match!')
            return render(request, 'signup.html')
        
        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            messages.info(request, 'User already exists!')
            return render(request, 'signup.html')
        else:
            user = User.objects.create_user(
                email=email, username=username, password=password)
            user.save()
            messages.success(request, 'User created successful')
            return redirect(signin)
    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    messages.info(request, "Successful logged out!")
    return redirect(signin)


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
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Appointment added successfully')
            return redirect(appointments)
        else:
            messages.error(request, 'Appointment not added')
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

    # form instance for mother monitoring
    first_time_patient_instance, _ = FirstTimePatientInfo.objects.get_or_create(pregnancy=pregnancey)
    first_pregnance_form = FirstTimePatientInfoForm(instance=first_time_patient_instance)

    previous_pregnancies_instance, _ = PreviousPregnancyInfo.objects.get_or_create(pregnancy=pregnancey)
    previous_pregnancies_form = PreviousPregnancyInfoForm(instance=previous_pregnancies_instance)

    labaratory_instance, _ = LaboratoryMeasurement.objects.get_or_create(pregnancy=pregnancey)
    labaratory_info_form = LaboratoryMeasurementForm(instance=labaratory_instance)

    attendance_instance, _ = AttendanceReport.objects.get_or_create(pregnancy=pregnancey)
    attendance_report_form = AttendanceReportForm(instance=attendance_instance)

    # handling patient monitoring forms
    if request.method == "POST":
        if 'first_pregnancy_form_save' in request.POST:
            first_time_patient_instance, _ = FirstTimePatientInfo.objects.get_or_create(pregnancy=pregnancey)
            first_pregnance_form = FirstTimePatientInfoForm(request.POST, instance=first_time_patient_instance)
            if first_pregnance_form.is_valid():
                first_pregnance_form.save()
                messages.success(request, 'First time patient info saved successfully')
                return redirect('pregnance', id)
        
        elif 'previous_pregnancies_form_save' in request.POST:
            previous_pregnancies_instance, _ = PreviousPregnancyInfo.objects.get_or_create(pregnancy=pregnancey)
            previous_pregnancies_form = PreviousPregnancyInfoForm(request.POST, instance=previous_pregnancies_instance)
            if previous_pregnancies_form.is_valid():
                previous_pregnancies_form.save()
                messages.success(request, 'Previous pregnancies info saved successfully')
                return redirect('pregnance', id)
        
        elif 'labaratory_info_form_save' in request.POST:
            labaratory_instance, _ = LaboratoryMeasurement.objects.get_or_create(pregnancy=pregnancey)
            labaratory_info_form = LaboratoryMeasurementForm(request.POST, instance=labaratory_instance)
            if labaratory_info_form.is_valid():
                labaratory_info_form.save()
                messages.success(request, 'Labaratory info saved successfully')
                return redirect('pregnance', id)
        
        elif 'attendance_report_form_save' in request.POST:
            attendance_instance, _ = AttendanceReport.objects.get_or_create(pregnancy=pregnancey)
            attendance_report_form = AttendanceReportForm(request.POST, instance=attendance_instance)
            if attendance_report_form.is_valid():
                attendance_report_form.save()
                messages.success(request, 'Attendance report saved successfully')
                return redirect('pregnance', id)


    # Form instances for child monitoring
    first_attendance_instance, _ = ChildFirstAttendence.objects.get_or_create(pregnancy=pregnancey)
    first_attendance_form = ChildFirstAttendenceForm(instance=first_attendance_instance)
    
    vaccine_instance, _ = ChildVaccineInfo.objects.get_or_create(pregnancy=pregnancey)
    vaccine_form = ChildVaccineInfoForm(instance=vaccine_instance)
    
    attendance_instance, _ = ChildMonitoringAttendance.objects.get_or_create(pregnancy=pregnancey)
    attendance_monitor_form = ChildMonitoringAttendanceForm(instance=attendance_instance)

    # Handling child monitoring forms
    if request.method == "POST":
        # Child first attendance form
        if 'first_attendance_form_save' in request.POST:
            first_attendance_instance, _ = ChildFirstAttendence.objects.get_or_create(pregnancy=pregnancey)
            first_attendance_form = ChildFirstAttendenceForm(request.POST, instance=first_attendance_instance)
            if first_attendance_form.is_valid():
                first_attendance_form.save()
                messages.success(request, 'First time child info saved successfully')
                return redirect('pregnance', id)
        # Child vaccine info form
        elif 'vaccine_form_save' in request.POST:
            vaccine_instance, _ = ChildVaccineInfo.objects.get_or_create(pregnancy=pregnancey)
            vaccine_form = ChildVaccineInfoForm(request.POST, instance=vaccine_instance)
            if vaccine_form.is_valid():
                vaccine_form.save()
                messages.success(request, 'Vaccine info saved successfully')
                return redirect('pregnance', id)
        # Child monitoring attendance form
        elif 'attendance_monitor_form_save' in request.POST:
            attendance_instance, _ = ChildMonitoringAttendance.objects.get_or_create(pregnancy=pregnancey)
            attendance_monitor_form = ChildMonitoringAttendanceForm(request.POST, instance=attendance_instance)
            if attendance_monitor_form.is_valid():
                attendance_monitor_form.save()
                messages.success(request, 'Attendance saved successfully')
                return redirect('pregnance', id)

    # Set up context
    context = {
        'pregnancey': pregnancey,
        'first_pregnance_form': first_pregnance_form,
        'previous_pregnancies_form': previous_pregnancies_form,
        'labaratory_info_form': labaratory_info_form,
        'attendance_report_form': attendance_report_form,
        'first_attendance_form': first_attendance_form,
        'vaccine_form': vaccine_form,
        'attendance_monitor_form': attendance_monitor_form
    }
    return render(request, 'pregnance.html', context)

    

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

    context = {"weight": child_weight, "pregnancy": pregnancy, 'form': form, 'weight_data_json': json_data}
    return render(request, 'child_data.html', context)


def reports(request):
    pregnancies = Pregnancy.objects.all()
    attendance_reports = AttendanceReport.objects.all()
    
    # Perform any processing or calculations on the data here
    
    context = {
        'pregnancies': pregnancies,
        'attendance_reports': attendance_reports,
        # Add any other processed data you want to pass to the template
    }
    return render(request, 'report.html', context)