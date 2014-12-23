"""
urls for FHIR RestAPI
Version 0.1.
Link in to host site at "/api/1.0/"

"""
__author__ = 'mark'
from django.conf.urls import patterns, include, url
from views import ApiPatient_Create, ApiPatient_Read, ApiPatient_vread
from rest_framework import routers
from rest_framework import permissions

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()

#import fhir_rest.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),



    # Patient Processing
    # Id and version id is 36 character regex: [a-z0-9\-\.]{1,36}
    url(r'^patient/$', ApiPatient_Create.as_view()) , #'fhir_rest.views.patient_create'),
    url(r'^patient/(?P<patient_id>\w[a-z0-9\-\.]{1,36})/$', ApiPatient_Read.as_view() ),   # fhir_rest.views.patient_read

    url(r'^patient/(?P<patient_id>\w+)/_history/(?P<version_id>\w+)/$', ApiPatient_vread.as_view() ), #'fhir_rest.views.patient_vread'),



)
