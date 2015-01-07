"""
bbp_rest
FILE: fhir_patient.renderers
Created: 1/7/15 3:21 PM

Attempting to create new Media Type support
- application/xml+fhir
- application/json+fhir
- application/atom+xml


"""
__author__ = 'Mark Scrimshire:@ekivemark'

from rest_framework.renderers import JSONRenderer
from rest_framework.renderers import XMLRenderer


class FHIRJRenderer(JSONRenderer):
    """

    Renderer which serializes to JSON.

    media_type = application/json+fhir

    """
    media_type = 'application/json+fhir'
    format = 'json+fhir'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders into json
        """
        renderer_context = renderer_context or {}

        json = super(FHIRJRenderer, self).render(data, accepted_media_type,
                                                 renderer_context)
        return json


class FHIRARenderer(XMLRenderer):
    """

    Renderer which serializes to ATOM/XML.

    media_type = application/atom+xml

    """
    media_type = 'application/atom+xml'
    format = 'atom+xml'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders into xml
        """
        renderer_context = renderer_context or {}

        atom = super(FHIRARenderer, self).render(data, accepted_media_type,
                                                 renderer_context)
        return atom


class FHIRXRenderer(XMLRenderer):
    """

    Renderer which serializes to XML.

    media_type = application/xml+fhir

    """
    media_type = 'application/xml+fhir'
    format = 'xml+fhir'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders into xml
        """
        renderer_context = renderer_context or {}

        xml = super(FHIRXRenderer, self).render(data, accepted_media_type,
                                                 renderer_context)
        return xml

