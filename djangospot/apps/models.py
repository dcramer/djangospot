from django.db import models
from djangospot.utils.fields import *
from tagging.fields import TagField

from django.contrib.auth.models import User

LOCALES = (
    ('en', 'English'),
)

class License(models.Model):
    license_id          = UUIDField(auto=True)
    name                = models.CharField(max_length=128, unique=True)
    description         = models.TextField()

    def __unicode__(self):
        return self.name

class Category(models.Model):
    license_id          = UUIDField(auto=True)
    name                = models.CharField(max_length=128, unique=True)
    description         = models.TextField()

    def __unicode__(self):
        return self.name

class App(models.Model):
    app_id              = UUIDField(auto=True)
    name                = models.CharField(max_length=128)
    description         = models.TextField()
    license             = models.ForeignKey(License, blank=True, null=True)
    license_name        = models.CharField(max_length=128)
    license_description = models.TextField()
    tags                = TagField(blank=True, null=True)
    website             = models.URLField(verify_exists=False)
    owner               = models.ForeignKey(User)
    # TODO: we should improve this and create some kind of denormalized M2M field
    categories          = models.ManyToManyField(Category)
    category_ids        = SeperatedValuesField()
    roles               = models.ManyToManyField(User, through="AppRole")
    locales             = SeperatedValuesField(blank=True, null=True)
    date_added          = CreatedDateTimeField(editable=False)
    date_changed        = ModifiedDateTimeField(editable=False)

    def __unicode__(self):
        return self.name

class AppRole(models.Model):
    app                 = models.ForeignKey(App)
    user                = models.ForeignKey(User)
    role                = models.IntegerField(choices=AppRole.levels, default=10)
    
    levels = (
        (10, 'Maintainer'),
        (20, 'Admin'),
    )
    
    class Meta:
        db_table = 'apps_app__roles'