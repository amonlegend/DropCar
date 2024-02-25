from datetime import date
import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

#Create your model here

#Checking validation about the contact number
def validate_contact(value):
    if not value.isdigit():
        raise ValidationError('Please enter only digits for contact number')
    if len(value) != 10:
        raise ValidationError('Contact number must be exactly 10 digits')
    if not value.startswith('9'):
        raise ValidationError('Contact number must start with 9')

#creating a User which extends Django Abstract User table
class User(AbstractUser):
    full_name = models.CharField(max_length=335)
    phone = models.CharField(max_length=10,validators=[validate_contact])
    # address = models.CharField(max_length=225,default="")
    # dob = models.DateField(null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    def __str__(self):
        return self.username