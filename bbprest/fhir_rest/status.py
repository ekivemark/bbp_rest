"""
Descriptive HTTP status codes, for code readability.
Based on Django_rest Framework and extended for FHIR API responses
http://www.django-rest-framework.org/#

See RFC 2616 - http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
And RFC 6585 - http://tools.ietf.org/html/rfc6585
"""
from __future__ import unicode_literals
__author__ = 'mark'


def is_informational(code):
    return code >= 100 and code <= 199


def is_success(code):
    return code >= 200 and code <= 299


def is_redirect(code):
    return code >= 300 and code <= 399


def is_client_error(code):
    return code >= 400 and code <= 499


def is_server_error(code):
    return code >= 500 and code <= 599


HTTP_100_CONTINUE = 100
HTTP_101_SWITCHING_PROTOCOLS = 101
# 200 update | validate
# successful update (if allowed)
HTTP_200_OK = 200
# 201 update | create | transaction
# successful create (if allowed)
HTTP_201_CREATED = 201
HTTP_202_ACCEPTED = 202
HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
# 204 delete
# returned after successful deletion
# OperationOutcome resource with NO errors can be returned
# Also returned for deletion request on already deleted resource
HTTP_204_NO_CONTENT = 204
HTTP_205_RESET_CONTENT = 205
HTTP_206_PARTIAL_CONTENT = 206
HTTP_300_MULTIPLE_CHOICES = 300
HTTP_301_MOVED_PERMANENTLY = 301
HTTP_302_FOUND = 302
HTTP_303_SEE_OTHER = 303
HTTP_304_NOT_MODIFIED = 304
HTTP_305_USE_PROXY = 305
HTTP_306_RESERVED = 306
HTTP_307_TEMPORARY_REDIRECT = 307
# 400 update | create | search | validate
# Resource could not be parsed
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_402_PAYMENT_REQUIRED = 402
HTTP_403_FORBIDDEN = 403
# 404 read | update | create | search | conformance
# Unknown Resource or Resource Not Supported
# or not a FHIR endpoint
HTTP_404_NOT_FOUND = 404
# 405 vread | delete | search
# access previous versions not allowed
# Resource did not exist exist prior to update
# and client defined ids are not allowed
# server may refuse deletion requests
HTTP_405_METHOD_NOT_ALLOWED = 405
HTTP_406_NOT_ACCEPTABLE = 406
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407
HTTP_408_REQUEST_TIMEOUT = 408
# 409 update
# version update conflict
# Returned if deletion is allowed but Resource-specific
# referential integrity creates an error
HTTP_409_CONFLICT = 409
# 410 read | vread | delete
# Deleted Resource
HTTP_410_GONE = 410
HTTP_411_LENGTH_REQUIRED = 411
# 412 update
# Incorrect version id supplied
HTTP_412_PRECONDITION_FAILED = 412
HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413
HTTP_414_REQUEST_URI_TOO_LONG = 414
HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416
HTTP_417_EXPECTATION_FAILED = 417
# 422 update | create | validate
# FHIR SPECIFIC EXCEPTION
# business rules preclude update
# unprocessable entity. server business rules violated
# return with OperationsOutcome resource for additional detail
HTTP_422_UNPROCESSABLE_ENTITY = 422

HTTP_428_PRECONDITION_REQUIRED = 428
HTTP_429_TOO_MANY_REQUESTS = 429
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
HTTP_500_INTERNAL_SERVER_ERROR = 500
HTTP_501_NOT_IMPLEMENTED = 501
HTTP_502_BAD_GATEWAY = 502
HTTP_503_SERVICE_UNAVAILABLE = 503
HTTP_504_GATEWAY_TIMEOUT = 504
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511

