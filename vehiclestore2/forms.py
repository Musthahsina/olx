from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from vehiclestore2.models import Vehicles

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class LoginForm(forms.Form):

    username=forms.CharField()
    password=forms.CharField()

class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=["vehicle_name","vehicle_number","vehicle_model","owner_name","kms_run","image"]

class VehicleChangeForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=["vehicle_name","vehicle_number","vehicle_model","owner_name","kms_run","image"]

    
    

