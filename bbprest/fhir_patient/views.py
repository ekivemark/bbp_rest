from django.shortcuts import render
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from django.conf import settings as CONFIG
from . import status

from .tools import valid_patient
"""
App: fhir_patient
Created: 12/18/2014 11:36am ET

Author: Mark Scrimshire:@ekivemark

Creating this app as the integration point for Patient/Beneficiary/Member
information access and presentation

This app will present a series of modules in tools.py. These will be
used by the fhir_rest interface.

The objective is to split out the data extract functions from the
REST Api presentations. This should allow other organizations to replace
the modules with extract routines tailored to their specific environment.

"""
# Create your views here.
class ApiTestPoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        print "hello endpoint test"
        return HttpResponse('Hello, OAuth2!')


class ApiPatient_Read(ProtectedResourceView):
    def get(self, request, patient_id, *args, **kwargs):

    # Test patient_id for valid format
    # Id and version id is 36 character regex: [a-z0-9\-\.]{1,36}
    # This was evaluated in urls.py before being passed to this function
    # invalid formats have already returned a 404

    # Now we can Test for compliance with PHIR call format:
    # Request Type = GET
        request_type = request.method

    # Then we can do a lookup for patient_id
    # We return 410 if resource has been deleted
    # We return 404 if not found

        patient_test = valid_patient(patient_id)

        if CONFIG.DEBUG == True:
            print "Valid Patient: [%s]" % patient_test

    # If valid patient_id is found we display it.


    # We need to evaluate the call parameter
    # _format=[mime-type]
    #  to return JSON or XML document.

    # Set a default status code
        result = status.HTTP_200_OK

        back_at_you = '[%s]%s Patient Read request for %s' % (request_type, patient_test, patient_id)

        if CONFIG.DEBUG == True:
            print "Patient Id:[%s] " % patient_id
            print "Request: %s" % request_type
            print "%s with status: %s" % (back_at_you, result)

        return HttpResponse(back_at_you, status=result)

class ApiPatient_Read_Version(ProtectedResourceView):
    def get(self, request, patient_id, version_id, *args, **kwargs):

        print "In Api_Patient_Read_Version"

        # Now we can Test for compliance with PHIR call format:
        # Request Type = GET
        request_type = request.method

        # Then we can do a lookup for patient_id
        # We return 410 if resource has been deleted
        # We return 404 if not found

        patient_test = valid_patient(patient_id)
        version = version_id


        if CONFIG.DEBUG == True:
            print "Valid Patient: [%s]" % patient_test
            print "Version %s" % version


        return HttpResponse(patient_test, patient_id, version, request_type)