from coffin.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    url(r'^', IndexController(), name='apps.index'),
    url(r'submit^', SubmitController(), name='apps.submit'),
)