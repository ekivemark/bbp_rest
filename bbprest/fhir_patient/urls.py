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

from rest_framework.urlpatterns import format_suffix_patterns
from views import BeneficiaryViewSet
from views import BeneficiaryDetail
from views import BeneficiaryDetail_Version
from rest_framework import renderers

beneficiary_list = BeneficiaryViewSet.as_view({
    'get':'list',
    'post':'create'
})

detail_mode = {'get':'retrieve','post':'create'}

urlpatterns = format_suffix_patterns([
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/', ApiTestPoint.as_view()),  # and also a resource server!


    # Patient Processing
    # Id and version id is 36 character regex: [a-z0-9\-\.]{1,36}
    url(r'^patient/$', beneficiary_list, name='beneficiary-list'),
    url(r'^patient/(?P<id>\w[a-z0-9\-\.]{1,36})/$', BeneficiaryDetail.as_view(lookup_field='id'), name='beneficiary-detail'),

    url(r'^patient/(?P<id>\w+)/_history/(?P<version_id>\w[0-9\-\.])/$', BeneficiaryDetail.as_view(lookup_field='id'), name='beneficiary-version' ),

])
