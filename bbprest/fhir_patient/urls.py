"""
bbp_rest - URLS for FHIR_Patient via BBP
FILE: urls
Created: 12/30/14 4:31 PM

Version 0.1.
Link in to host site at "/api/1.0/"

Implementing FHIR Spec v0.0.82
http://www.hl7.org/implement/standards/fhir/http.html

The following logical interactions are defined:

Instance Level Interactions:
read	Read the current state of the resource
vread	Read the state of a specific version of the resource
update	Update an existing resource by its id (or create it if it is new)
delete	Delete a resource
history	Retrieve the update history for a particular resource
Type Level Interactions
create	Create a new resource with a server assigned id
search	Search the resource type based on some filter criteria
history	Retrieve the update history for a particular resource type
validate	Check that the content would be acceptable as an update
Whole System Interactions
conformance	Get a conformance statement for the system
transaction	Update, create or delete a set of resources as a single transaction
history	Retrieve the update history for all resources
search	Search across all resource types based on some filter criteria

Status: Embedded in APITestPoint.as_view()

"""
__author__ = 'Mark Scrimshire:@ekivemark'

from django.conf.urls import patterns, include, url
from views import *

from rest_framework.urlpatterns import format_suffix_patterns
from views import ApiStatus
from views import BeneficiaryViewSet
from views import BeneficiaryDetailViewSet
from views import BeneficiaryVersionViewSet


beneficiary_list = BeneficiaryViewSet.as_view({
    'get':'list',
    'post':'create'
})

detail_mode = {'get':'retrieve',
#               'post':'create',
               }

version_mode = {'get':'version_retrieve',
#                'post':'create',
}

beneficiary_detail = BeneficiaryDetailViewSet.as_view(detail_mode)

beneficiary_detail_version = BeneficiaryVersionViewSet.as_view(version_mode)


urlpatterns = format_suffix_patterns([
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^status/', ApiStatus, name="api-status"),  # and also a resource server!


    # Patient Processing
    # Id and version id is 36 character regex: [a-z0-9\-\.]{1,36}


    # List of all beneficiaries is not supported in FHIR spec.for
    # This call is for testing purposes.
    # It will be disabled resulting in a 404
    url(r'^patient/$', beneficiary_list, name='beneficiary-list'),

    # vread functionality. Enables read of a specific version of a record.
    url(r'^patient/(?P<id>\w[a-z0-9\-\.]{1,36})/_history/(?P<version>\w[A-Z0-9\-\.\:]{1,28})/$', beneficiary_detail_version, name='beneficiary-version' ),
    # read functionality. Enables read of a single beneficiary record.
    url(r'^patient/(?P<id>\w[a-z0-9\-\.]{1,36})/$', beneficiary_detail, name='beneficiary-detail'),

])
