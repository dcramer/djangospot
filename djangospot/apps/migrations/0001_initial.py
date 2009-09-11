
from south.db import db
from django.db import models
from djangospot.apps.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('apps_category', (
            ('id', orm['apps.Category:id']),
            ('license_id', orm['apps.Category:license_id']),
            ('name', orm['apps.Category:name']),
            ('description', orm['apps.Category:description']),
        ))
        db.send_create_signal('apps', ['Category'])
        
        # Adding model 'License'
        db.create_table('apps_license', (
            ('id', orm['apps.License:id']),
            ('license_id', orm['apps.License:license_id']),
            ('name', orm['apps.License:name']),
            ('description', orm['apps.License:description']),
        ))
        db.send_create_signal('apps', ['License'])
        
        # Adding model 'AppRole'
        db.create_table('apps_app__roles', (
            ('id', orm['apps.AppRole:id']),
            ('app', orm['apps.AppRole:app']),
            ('user', orm['apps.AppRole:user']),
            ('role', orm['apps.AppRole:role']),
        ))
        db.send_create_signal('apps', ['AppRole'])
        
        # Adding model 'App'
        db.create_table('apps_app', (
            ('id', orm['apps.App:id']),
            ('app_id', orm['apps.App:app_id']),
            ('name', orm['apps.App:name']),
            ('description', orm['apps.App:description']),
            ('license', orm['apps.App:license']),
            ('license_name', orm['apps.App:license_name']),
            ('license_description', orm['apps.App:license_description']),
            ('tags', orm['apps.App:tags']),
            ('website', orm['apps.App:website']),
            ('owner', orm['apps.App:owner']),
            ('category_ids', orm['apps.App:category_ids']),
            ('locales', orm['apps.App:locales']),
            ('date_added', orm['apps.App:date_added']),
            ('date_changed', orm['apps.App:date_changed']),
            ('rating_overall_votes', orm['apps.App:rating_overall_votes']),
            ('rating_overall_score', orm['apps.App:rating_overall_score']),
        ))
        db.send_create_signal('apps', ['App'])
        
        # Adding ManyToManyField 'App.categories'
        db.create_table('apps_app_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('app', models.ForeignKey(orm.App, null=False)),
            ('category', models.ForeignKey(orm.Category, null=False))
        ))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('apps_category')
        
        # Deleting model 'License'
        db.delete_table('apps_license')
        
        # Deleting model 'AppRole'
        db.delete_table('apps_app__roles')
        
        # Deleting model 'App'
        db.delete_table('apps_app')
        
        # Dropping ManyToManyField 'App.categories'
        db.delete_table('apps_app_categories')
        
    
    
    models = {
        'apps.app': {
            'app_id': ('iplatform.core.fields.idtypes.UUIDField', [], {'version': '4', 'auto': 'True', 'max_length': '32', 'blank': 'True', 'unique': 'True', 'name': "'app_id'"}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['apps.Category']"}),
            'category_ids': ('djangospot.utils.fields.SeparatedValuesField', [], {'token': "','"}),
            'date_added': ('CreatedDateTimeField', [], {'editable': 'False'}),
            'date_changed': ('ModifiedDateTimeField', [], {'editable': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['apps.License']", 'null': 'True', 'blank': 'True'}),
            'license_description': ('django.db.models.fields.TextField', [], {}),
            'license_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'locales': ('djangospot.utils.fields.SeparatedValuesField', [], {'token': "','", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_app_set'", 'null': 'True', 'to': "orm['auth.User']"}),
            'rating_overall_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_overall_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']"}),
            'tags': ('TagField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'apps.approle': {
            'Meta': {'db_table': "'apps_app__roles'"},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['apps.App']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'apps.category': {
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('iplatform.core.fields.idtypes.UUIDField', [], {'version': '4', 'auto': 'True', 'max_length': '32', 'blank': 'True', 'unique': 'True', 'name': "'license_id'"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'apps.license': {
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'license_id': ('iplatform.core.fields.idtypes.UUIDField', [], {'version': '4', 'auto': 'True', 'max_length': '32', 'blank': 'True', 'unique': 'True', 'name': "'license_id'"}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['apps']
