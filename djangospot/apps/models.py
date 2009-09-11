from django.db import models
from djangospot.utils.fields import *
from tagging.fields import TagField
from djangoratings.fields import RatingField

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
    # If the app has not been claimed then there is no owner.
    owner               = models.ForeignKey(User, blank=True, null=True)
    # TODO: we should improve this and create some kind of denormalized M2M field
    categories          = models.ManyToManyField(Category)
    category_ids        = SeparatedValuesField()
    roles               = models.ManyToManyField(User, through="AppRole")
    locales             = SeparatedValuesField(blank=True, null=True)
    rating_overall      = RatingField(range=5)
    date_added          = CreatedDateTimeField(editable=False)
    date_changed        = ModifiedDateTimeField(editable=False)

    def __unicode__(self):
        return self.name

class AppRole(models.Model):
    levels = (
        (10, 'Maintainer'),
        (20, 'Admin'),
    )
    
    app                 = models.ForeignKey(App)
    user                = models.ForeignKey(User)
    role                = models.IntegerField(choices=levels, default=10)
    
    class Meta:
        db_table = 'apps_app__roles'