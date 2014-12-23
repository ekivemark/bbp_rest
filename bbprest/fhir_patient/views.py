from django.shortcuts import render
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
