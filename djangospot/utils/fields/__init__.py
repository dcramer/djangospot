# -*- encoding: utf-8 -*-

from django.db import models

from djangospot.utils import forms as forms_ext
from djangospot.utils import json

import datetime
import uuid

class UUIDField(models.Field):
    """
        A field which stores a UUID value in hex format. This may also have
        the Boolean attribute 'auto' which will set the value on initial save to a
        new UUID value (calculated using the UUID1 method). Note that while all
        UUIDs are expected to be unique we enforce this with a DB constraint.
    """
    # __metaclass__ = models.SubfieldBase

    def __init__(self, version=4, node=None, clock_seq=None, namespace=None, name=None, auto=False, *args, **kwargs):
        assert(version in (1, 3, 4, 5), "UUID version %s is not supported." % (version,))
        self.auto = auto
        self.version = version
        # We store UUIDs in hex format, which is fixed at 32 characters.
        kwargs['max_length'] = 32
        if auto:
            # Do not let the user edit UUIDs if they are auto-assigned.
            kwargs['editable'] = False
            kwargs['blank'] = True
            kwargs['unique'] = True
        if version == 1:
            self.node, self.clock_seq = node, clock_seq
        elif version in (3, 5):
            self.namespace, self.name = namespace, name
        super(UUIDField, self).__init__(*args, **kwargs)

    def _create_uuid(self):
        if self.version == 1:
            args = (self.node, self.clock_seq)
        elif self.version in (3, 5):
            args = (self.namespace, self.name)
        else:
            args = ()
        return getattr(uuid, 'uuid%s' % (self.version,))(*args)

    def db_type(self):
        return 'char(%s)' % (self.max_length,)

    def pre_save(self, model_instance, add):
        """ see CharField.pre_save
            This is used to ensure that we auto-set values if required.
        """
        value = getattr(model_instance, self.attname, None)
        if self.auto and add and not value:
            # Assign a new value for this attribute if required.
            value = self._create_uuid().hex
            setattr(model_instance, self.attname, value)
        return value

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        from south.modelsinspector import introspector
        field_class = "djangospot.utils.fields.UUIDField"
        args, kwargs = introspector(self)
        for kw in ('auto', 'version', 'node', 'clock_seq', 'namespace', 'name'):
            val = getattr(self, kw, None)
            if val:
                kwargs[kw] = repr(val)
        return (field_class, args, kwargs)

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

class AutoSlugField(models.CharField):
    def __init__(self, for_field, *args, **kwargs):
        self.for_field = for_field
        super(AutoSlugField, self).__init__(*args, **kwargs)
    
    def pre_save(self, model_instance, add):
        from django.template.defaultfilters import slugify
        
        value_to_slugify = getattr(model_instance, self.for_field)
        return slugify(value_to_slugify)

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