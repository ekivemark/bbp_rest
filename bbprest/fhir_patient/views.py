from django.shortcuts import render
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from django.conf import settings as CONFIG
from . import status

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import XMLRenderer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.decorators import api_view
from renderers import FHIRJRenderer
from renderers import FHIRARenderer
from renderers import FHIRXRenderer


from models import Beneficiary
from serializers import BeneficiarySerializer


from .tools import valid_patient
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



class BeneficiaryViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):

    renderer_classes = (FHIRJRenderer,
                        FHIRARenderer,
                        FHIRXRenderer,
                        BrowsableAPIRenderer,
                        TemplateHTMLRenderer,
                        JSONRenderer,
                        XMLRenderer)

    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer

    def list(self, request):
        print "in list"
        queryset = Beneficiary.objects.all()
        serializer = BeneficiarySerializer(queryset, many=True)
        return Response(serializer.data)


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BeneficiaryDetailViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):

    renderer_classes = (FHIRJRenderer,
                        FHIRARenderer,
                        FHIRXRenderer,
                        BrowsableAPIRenderer,
                        TemplateHTMLRenderer,
                        JSONRenderer,
                        XMLRenderer)

    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer

    def retrieve(self, request, id=None, *args, **kwargs):
        print "in retrieve"
        print "ID: %s" % id


        queryset = Beneficiary.objects.all()
        beneficiary = get_object_or_404(queryset, id=id)
        serializer = BeneficiarySerializer(beneficiary)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        print "in create"
        return self.retrieve(request, *args, **kwargs)

#    def post(self, request, *args, **kwargs):
#        print "in post"
#        return self.retrieve(request, *args, **kwargs)


class BeneficiaryVersionViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):

    renderer_classes = (FHIRJRenderer,
                        FHIRARenderer,
                        FHIRXRenderer,
                        BrowsableAPIRenderer,
                        TemplateHTMLRenderer,
                        JSONRenderer,
                        XMLRenderer)

    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer

    def version_retrieve(self, request, id=None, version=None):
        print "in version retrieve"
        queryset = Beneficiary.objects.all()
        beneficiary_list = queryset.filter(pk=id)

        #beneficiary_version = beneficiary_list.filter(version=version)
        beneficiary_version = get_object_or_404(beneficiary_list, version=version)

        serializer = BeneficiarySerializer(beneficiary_version)
        return Response(serializer.data)


    def get(self, request, *args, **kwargs):
        return self.version_retrieve(request, *args, **kwargs)

@api_view(('GET',))
def ApiStatus(request, format=None):

    status = "FHIR Specification API Status. " \
             "Data source: Pre-prototype. " \
             "read. vread."

    return Response({
        'status': status,
    })
