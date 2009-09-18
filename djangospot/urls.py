from coffin.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^', include('djangospot.apps.urls')),
    url(r'^snippets/', include('djangospot.snippets.urls')),
    
)
