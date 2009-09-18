from coffin.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^$', views.IndexController(), name='snippets.index'),
    url(r'^submit/$', views.SubmitController(), name='snippets.submit'),
)
