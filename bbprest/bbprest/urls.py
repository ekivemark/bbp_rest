from django.conf.urls import patterns, include, url
from django.contrib import admin

#from .views import ApiEndpoint
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbprest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')), # look ma, I'm a provider!
    #url(r'^api/hello', ApiEndpoint.as_view()),  # and also a resource server!

    # API
    url(r'^api/1.0/', include('fhir_rest.urls', namespace='bb_fhir')),

    url(r'^admin/', include(admin.site.urls)),
)
