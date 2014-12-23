from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.http import HttpResponse, Http404
from . import status
from django.conf import settings as CONFIG
from fhir_patient.tools import *
from oauth2_provider.views.generic import ProtectedResourceView

# Create your views here.
# We will protect these views with OAUTH

class ApiPatient_Create(ProtectedResourceView):
    def get(request):
        """

    Operation: POST

    This implementation is not processing patient updates
    Therefore: return error code: 422 Unprocessable Entity -

    the proposed resource violated applicable FHIR profiles or server
    business rules. This should be accompanied by an OperationOutcome
    resource providing additional detail

    http://www.hl7.org/implement/standards/fhir/operationoutcome.html
<OperationOutcome xmlns="http://hl7.org/fhir"> doco
 <!-- from Resource: extension, modifierExtension, language, text, and contained -->
 <issue>  <!-- 1..* A single issue associated with the action -->
  <severity value="[code]"/><!-- 1..1 fatal | error | warning | information -->
  <type><!-- 0..1 Coding Error or warning code --></type>
  <details value="[string]"/><!-- 0..1 Additional description of the issue -->
  <location value="[string]"/><!-- 0..* XPath of element(s) related to issue -->
 </issue>
</OperationOutcome>

    :param request:

    :return:
        """
        request_type = request.method

        if CONFIG.DEBUG == True:
            print "Request: %s" % request_type


        back_at_you = '[%s]Create functions for entity PATIENT are disabled' % request_type

        return HttpResponse(back_at_you , status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ApiPatient_Read(ProtectedResourceView):
    def get(request,patient_id ):


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

        if CONFIG.DEBUG == True:
            print "Patient Id:[%s] " % patient_id
            print "Request: %s" % request_type


        back_at_you = '[%s]%s Patient Read request for %s' % (request_type, patient_test, patient_id)

        return HttpResponse(back_at_you, status=result)


class ApiPatient_vread(ProtectedResourceView):
    def get(request, patient_id, version_id ):

        request_type = request.method

    # Set a default status code
        result = status.HTTP_200_OK

        if CONFIG.DEBUG == True:
            print "[%s]Patient Id:[%s] document version:[%s] " % (request_type, patient_id, version_id)
            print "Request: %s" % request_type

        back_at_you = '[%s]Patient Read request for %s with Document version: %s' % (request_type, patient_id, version_id)

        return HttpResponse(back_at_you, status=result)



