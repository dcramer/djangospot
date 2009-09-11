from coffin.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^', views.IndexController(), name='apps.index'),
    url(r'submit^', views.SubmitController(), name='apps.submit'),
)