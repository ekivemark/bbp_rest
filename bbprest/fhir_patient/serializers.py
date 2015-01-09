"""
bbp_rest
FILE: fhir_patient/serializers
Created: 1/5/15 5:30 PM

Integrating fhir and django-rest-framework


"""
__author__ = 'Mark Scrimshire:@ekivemark'

from rest_framework import serializers

from models import Beneficiary

class BeneficiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Beneficiary
        fields = ('id','first_name', 'last_name',
        'date_of_birth','address_line_1',
    'address_line_2', 'city', 'state', 'zip',
    'country', 'phone', 'email', 'latest','version',
        )