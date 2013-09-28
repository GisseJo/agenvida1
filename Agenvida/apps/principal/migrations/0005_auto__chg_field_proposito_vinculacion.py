# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Proposito.vinculacion'
        db.alter_column('principal_proposito', 'vinculacion_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['principal.Vinculacion']))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Proposito.vinculacion'
        raise RuntimeError("Cannot reverse this migration. 'Proposito.vinculacion' and its values cannot be restored.")

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'principal.marcacion': {
            'Meta': {'object_name': 'Marcacion'},
            'cumplimiento': ('django.db.models.fields.IntegerField', [], {}),
            'dia': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proposito': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'marcaciones'", 'to': "orm['principal.Proposito']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'marcaciones'", 'to': "orm['auth.User']"})
        },
        'principal.proposito': {
            'Meta': {'object_name': 'Proposito'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes_ano': ('django.db.models.fields.DateField', [], {}),
            'proposito': ('django.db.models.fields.TextField', [], {}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'propositos'", 'to': "orm['auth.User']"}),
            'vinculacion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'propositos'", 'null': 'True', 'to': "orm['principal.Vinculacion']"})
        },
        'principal.tipo_marcacion': {
            'Meta': {'object_name': 'Tipo_marcacion'},
            'RangoInf': ('django.db.models.fields.IntegerField', [], {}),
            'RangoSup': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'principal.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contrato_pedagogico': ('django.db.models.fields.TextField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'grupo_de_vida': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideal_personal': ('django.db.models.fields.TextField', [], {}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'principal.vinculacion': {
            'Meta': {'object_name': 'Vinculacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vinculacion': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['principal']