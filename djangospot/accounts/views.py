import inspect

from registration.views import *

from coffin.shortcuts import render_to_response
from coffin.template import RequestContext

exec inspect.getsource(activate)
exec inspect.getsource(register)