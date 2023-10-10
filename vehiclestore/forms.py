from django import forms
from vehiclestore.models import Vehicles
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):

    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))



class VehicleCreateForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields="__all__"

        widgets={
            "vehicle_name":forms.TextInput(attrs={"class":"form-control"}),
            "vehicle_number":forms.TextInput(attrs={"class":"form-control"}),
            "vehicle_model":forms.TextInput(attrs={"class":"form-control"}),
            "owner_name":forms.TextInput(attrs={"class":"form-control"}),
            "kms_run":forms.TextInput(attrs={"class":"form-control"}),
            

            
        }

class VehicleChangeForm(forms.ModelForm):

    class Meta:
        model=Vehicles
        fields="__all__"

        widgets={
            "vehicle_name":forms.TextInput(attrs={"class":"form-control"}),
            "vehicle_number":forms.TextInput(attrs={"class":"form-control"}),
            "vehicle_model":forms.TextInput(attrs={"class":"form-control"}),
            "owner_name":forms.TextInput(attrs={"class":"form-control"}),
            "kms_run":forms.TextInput(attrs={"class":"form-control"}),
            "image":forms.FileInput(attrs={"class":"form-control"}),


            
        }

