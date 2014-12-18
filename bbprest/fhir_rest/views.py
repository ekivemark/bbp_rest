from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework import permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.http import HttpResponse, Http404
from . import status


# Create your views here.

def patient_create(request):
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

    print "Request: %s" % request_type

    back_at_you = '[%s]Create functions for entity PATIENT are disabled' % request_type

    return HttpResponse(back_at_you , status=status.HTTP_422_UNPROCESSABLE_ENTITY)

def patient_read(request,patient_id ):

    request_type = request.method

    # Set a default status code
    result = status.HTTP_200_OK

    print "Patient Id:[%s] " % patient_id
    print "Request: %s" % request_type

    back_at_you = '[%s]Patient Read request for %s' % (request_type, patient_id)

    return HttpResponse(back_at_you, status=result)


def patient_vread(request, patient_id, version_id ):

    request_type = request.method

    # Set a default status code
    result = status.HTTP_200_OK

    print "[%s]Patient Id:[%s] document version:[%s] " % (request_type, patient_id, version_id)
    print "Request: %s" % request_type

    back_at_you = '[%s]Patient Read request for %s with Document version: %s' % (request_type, patient_id, version_id)

    return HttpResponse(back_at_you, status=result)