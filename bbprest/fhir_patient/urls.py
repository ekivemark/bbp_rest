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
from views import BeneficiaryDetailViewSet
from views import BeneficiaryVersionViewSet


beneficiary_list = BeneficiaryViewSet.as_view({
    'get':'list',
    'post':'create'
})

detail_mode = {'get':'retrieve',
               'post':'create'}

version_mode = {'get':'version_retrieve',
                'post':'create'}

beneficiary_detail = BeneficiaryDetailViewSet.as_view(detail_mode)

beneficiary_detail_version = BeneficiaryVersionViewSet.as_view(version_mode)


urlpatterns = format_suffix_patterns([
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^test/', ApiTestPoint.as_view()),  # and also a resource server!


    # Patient Processing
    # Id and version id is 36 character regex: [a-z0-9\-\.]{1,36}
    url(r'^patient/$', beneficiary_list, name='beneficiary-list'),
    url(r'^patient/(?P<id>\w[a-z0-9\-\.]{1,36})/_history/(?P<version>\w[A-Z0-9\-\.\:]{1,28})/$', beneficiary_detail_version, name='beneficiary-version' ),
    url(r'^patient/(?P<id>\w[a-z0-9\-\.]{1,36})/$', beneficiary_detail, name='beneficiary-detail'),

])
