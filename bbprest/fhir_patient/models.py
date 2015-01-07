"""
bbp_rest - Models for FHIR_Patient
FILE: models.py
Created: 01/05/15 4:31 PM

Version 0.1.


"""
__author__ = 'Mark Scrimshire:@ekivemark'


from django.db import models
from localflavor.us.us_states import STATE_CHOICES
from django_countries.fields import CountryField

# Create your models here.


class Beneficiary(models.Model):
    id = models.BigIntegerField(primary_key=True)
    latest = models.BooleanField(default=True)
    version = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    date_of_birth = models.DateField(blank=True)
    address_line_1 = models.CharField(max_length=200, blank=True, default='')
    address_line_2 = models.CharField(max_length=200, blank=True, default='')
    city = models.CharField(max_length=150, blank=True, default='')
    state = models.CharField(choices=STATE_CHOICES ,max_length=30,null=True, blank=True)
    zip = models.CharField(max_length=30, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)



