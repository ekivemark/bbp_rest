from django.shortcuts import render
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404

from django.conf import settings as CONFIG
from . import status

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import XMLRenderer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.renderers import BrowsableAPIRenderer
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
class ApiTestPoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        print "hello endpoint test"
        return HttpResponse('Hello, OAuth2!')



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
        queryset = Beneficiary.objects.all()
        serializer = BeneficiarySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Beneficiary.objects.all()
        beneficiary = get_object_or_404(queryset, pk=pk)
        serializer = BeneficiarySerializer(beneficiary)
        return Response(serializer.data)


class BeneficiaryDetail(mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    """
    Retrieve a Beneficiary instance.
    """
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class BeneficiaryDetail_Version(mixins.RetrieveModelMixin):
    """
    Retrieve a Version of a Beneficiary record
    """
    queryset = Beneficiary.objects.all()
    serializer_class = BeneficiarySerializer

    def get(self, request, *args, **kwargs):
        print "ID: %s" % id
        print "Version: %s" % version_id

        return


