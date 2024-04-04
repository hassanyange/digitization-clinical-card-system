from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
@login_required
def home(request):
    
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect(signin)

    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        ##check if user already exists
        user = User.objects.filter(username=username).exists()
        if user:
            messages.info(request, 'User already exists')
            return render(request, 'signup.html')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.info(request, 'User created successful')
            return redirect(home)
    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return redirect(home)


##list all pattients
@login_required()
def patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})


##show one patient
@login_required
def patient(request, id):
    patient = Patient.objects.get(id=id)
    context = {'patient': patient}
    return render(request, 'patient.html', context)

##register new_patient
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


##edit patient
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


##delete patient
@login_required
def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect(patients)

