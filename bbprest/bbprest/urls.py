from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbprest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # OAuth Provider
    # http://django-oauth-toolkit.readthedocs.org/en/latest/tutorial/tutorial_01.html
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')), # look ma, I'm a provider!

    # Django Rest Framework tutorial
    url(r'^snip/', include('snippets.urls')),

    # API
    url(r'^api/1.0/', include('fhir_patient.urls', namespace='bb_fhir')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]