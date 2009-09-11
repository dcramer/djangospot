from coffin.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

    url(r'^', include('djangospot.apps.urls')),
)
