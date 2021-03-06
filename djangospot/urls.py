from coffin.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
import os.path

admin.autodiscover()

urlpatterns = patterns('',
    # media url for runserver
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    # django.contrib.admin
    url(r'^admin/media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(admin.__file__), 'media'), 'show_indexes': True}),
    url(r'^admin/', include(admin.site.urls)),

    # django-registration
    (r'^accounts/', include('djangospot.accounts.urls')),

    url(r'^', include('djangospot.apps.urls')),
    url(r'^snippets/', include('djangospot.snippets.urls')),
    
)
