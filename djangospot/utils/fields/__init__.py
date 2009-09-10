# -*- encoding: utf-8 -*-

from django.db import models

from djangospot.utils import forms as forms_ext
from djangospot.utils import json

import datetime

class JSONField(models.TextField):
    __metaclass__ = models.SubfieldBase
 
    def formfield(self, **kwargs):
        return super(JSONField, self).formfield(form_class=forms_ext.JSONField, **kwargs)
 
    def to_python(self, value):
        if isinstance(value, basestring):
            value = json.loads(value)
        return value
 
    def get_db_prep_save(self, value):
        if value is None: return
        return json.dumps(value)
 
    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.TextField"
        args, kwargs = introspector(self)
        return (field_class, args, kwargs)

class CreatedDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        # really we should check on ` and not model_instance.pk` also
        if not value:
            value = datetime.datetime.now()
        setattr(model_instance, self.attname, value)
        return value

class ModifiedDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        value = datetime.datetime.now()
        setattr(model_instance, self.attname, value)
        return value

class SeparatedValuesField(models.TextField):
    __metaclass__ = models.SubfieldBase

    def __init__(self, token=',', *args, **kwargs):
        self.token = token
        super(SeparatedValuesField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        return super(SeparatedValuesField, self).formfield(form_class=forms_ext.SeparatedValuesField, **kwargs)

    def to_python(self, value):
        if value is None: return []
        if isinstance(value, list):
            return value
        if not value:
            return []
        return unicode(value).split(self.token)

    def get_db_prep_value(self, value):
        if value is None: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join(filter(None, [unicode(s) for s in value]))

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        from south.modelsinspector import introspector
        field_class = "djangospot.utils.fields.SeparatedValuesField"
        args, kwargs = introspector(self)
        kwargs['token'] = repr(self.token)
        return (field_class, args, kwargs)