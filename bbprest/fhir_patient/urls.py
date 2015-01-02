"""
bbp_rest - URLS for FHIR_Patient via BBP
FILE: urls
Created: 12/30/14 4:31 PM

Version 0.1.
Link in to host site at "/api/1.0/"

"""
__author__ = 'Mark Scrimshire:@ekivemark'

from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/', ApiTestPoint.as_view()),  # and also a resource server!


    # Patient Processing
    # Id and version id is 36 character regex: [a-z0-9\-\.]{1,36}
    #url(r'^patient/$', ApiPatient_Create.as_view()) , #'fhir_rest.views.patient_create'),
    url(r'^patient/(?P<patient_id>\w[a-z0-9\-\.]{1,36})/$', ApiPatient_Read.as_view() ),
    url(r'^patient/(?P<patient_id>\w+)/_history/(?P<version_id>\w[0-9\-\.])/$', ApiPatient_Read_Version.as_view() ),


)
