"""
bbp_rest
FILE: tools
Created: 12/18/14 11:37 AM

Patient/Beneficiary/Member data interface tools
used by the fhir_rest API module

"""
from django.conf import settings as CONFIG
__author__ = 'Mark Scrimshire:@ekivemark'

def valid_patient(patient_id):

    result = "OTHER"

    valid_patient_ids = ('1234', '12345', '9876', '123456789012345678901234567890')
    deleted_patient_ids = ('4567','45678','abcd')

    if patient_id in valid_patient_ids:
        result = "VALID"
    elif patient_id in deleted_patient_ids:
        result = "DELETED"
    else:
        result = "INVALID"

    if CONFIG.DEBUG == True:
        print "Valid_Patient:Result: %s for %s" % (result, patient_id)

    return result

