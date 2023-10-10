from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehicles(models.Model):
    vehicle_name=models.CharField(max_length=200)
    vehicle_number=models.CharField(max_length=200)
    vehicle_model=models.CharField(max_length=200)
    owner_name=models.CharField(max_length=200)
    kms_run=models.PositiveIntegerField()
    image=models.ImageField(upload_to="images",null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

  
    def __str__(self):
        return self.vehicle_name