from coffin.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^$', views.IndexController(), name='apps.index'),
    url(r'^submit', views.SubmitController(), name='apps.submit'),
    url(r'^view/(?P<app_id>\d+)', views.ViewController(), name='apps.view'),
)
