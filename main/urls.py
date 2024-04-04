
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.logout_user, name='signout'),
    
    path('patients', views.patients, name='patients'),
    path('patient/<int:id>', views.patient, name='patient'),
    path('patient/new', views.new_patient, name='new_patient'),
    path('patient/<int:id>/edit', views.edit_patient, name='edit_patient'),
    path('patient/<int:id>/delete', views.delete_patient, name='delete_patient'),
    
]
