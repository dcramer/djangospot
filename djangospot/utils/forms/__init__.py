from django import forms
from django.utils import simplejson as json

class JSONWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        if not isinstance(value, basestring):
            value = json.dumps(value, indent=2)
        return super(JSONWidget, self).render(name, value, attrs)

class JSONField(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = JSONWidget
        super(JSONField, self).__init__(*args, **kwargs)
 
    def clean(self, value):
        if not value: return
        try:
            return json.loads(value)
        except Exception, exc:
            raise forms.ValidationError(u'JSON decode error: %s' % (unicode(exc),))

class SeparatedValuesWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        if value and not isinstance(value, basestring):
            value = ','.join(value)
        return super(SeparatedValuesWidget, self).render(name, value, attrs)

class SeparatedValuesField(forms.CharField):
    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        kwargs['widget'] = SeparatedValuesWidget
        super(SeparatedValuesField, self).__init__(*args, **kwargs)
 
    def clean(self, value):
        if not value: return
        return value.split(self.token)