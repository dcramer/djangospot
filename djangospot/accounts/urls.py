import inspect

from registration import urls

exec inspect.getsource(urls)\
    .replace('django.contrib.auth', 'coffin.contrib.auth')