"""
urls for FHIR RestAPI
Version 0.1.
Link in to host site at "/api/1.0/"

"""
__author__ = 'mark'
from django.conf.urls import patterns, include, url
from fhir_rest.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    # Patient Processing
    url(r'^patient/$', 'fhir_rest.views.patient_create'),
    url(r'^patient/(?P<patient_id>\w+)/$', 'fhir_rest.views.patient_read'),
    url(r'^patient/(?P<patient_id>\w+)/_history/(?P<version_id>\w+)/$', 'fhir_rest.views.patient_vread'),

)
