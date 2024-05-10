
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.logout_user, name='signout'),
    path('profile/', views.profile, name='profile'),
    
    path('patients', views.patients, name='patients'),
    path('patient/<int:id>', views.patient, name='patient'),
    path('patient/new', views.new_patient, name='new_patient'),
    path('patient/<int:id>/edit', views.edit_patient, name='edit_patient'),
    path('patient/<int:id>/delete', views.delete_patient, name='delete_patient'),
    
    path('doctors/', views.doctors, name='doctors'),
    path('doctor/<int:id>', views.doctor, name='doctor'),
    # path('doctor/new', views.new_doctor, name='new_doctor'),
    path('doctor/<int:id>/edit', views.edit_doctor, name='edit_doctor'),
    path('doctor/<int:id>/delete', views.delete_doctor, name='delete_doctor'),
    
    path('researchers/', views.researchers, name='researchers'),
    path('researcher/<int:id>', views.researcher, name='researcher'),
    #  path('researcher/new', views.researcher, name='new_researcher'),
    path('researcher/<int:id>/edit', views.researcher, name='edit_researcher'),
    path('researcher/<int:id>/delete', views.researcher, name='delete_researcher'),


    path('appointments/', views.appointments, name='appointments'),
    path('appointment/<int:id>', views.appointment, name='appointment'),
    # path('appointment/new', views.appointment, name='new_appointment'),
    path('appointment/<int:id>/edit', views.appointment, name='edit_appointment'),
    path('appointment/<int:id>/delete', views.appointment, name='delete_appointment'),

    path('patient/pregnance/<str:id>/', views.pregnance, name='pregnance'),
    path('child-data/<str:id>/', views.child_data, name='child-data'),
   
   
    path('reports/', views.reports, name='reports'),
    
    
]
