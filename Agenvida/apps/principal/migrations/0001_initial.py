# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'principal_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('ideal_personal', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('fecha_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('sexo', self.gf('django.db.models.fields.TextField')()),
            ('pais', self.gf('django.db.models.fields.TextField')(max_length=50)),
            ('grupo_de_vida', self.gf('django.db.models.fields.TextField')(max_length=140)),
            ('contrato_pedagogico', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'principal', ['UserProfile'])

        # Adding model 'Vinculacion'
        db.create_table(u'principal_vinculacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vinculacion', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'principal', ['Vinculacion'])

        # Adding model 'Proposito'
        db.create_table(u'principal_proposito', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('vinculacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Vinculacion'])),
            ('mes_ano', self.gf('django.db.models.fields.DateField')()),
            ('proposito', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'principal', ['Proposito'])

        # Adding model 'Marcacion'
        db.create_table(u'principal_marcacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proposito', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Proposito'])),
            ('dia', self.gf('django.db.models.fields.DateField')()),
            ('cumplimiento', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'principal', ['Marcacion'])

        # Adding model 'Tipo_marcacion'
        db.create_table(u'principal_tipo_marcacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('RangoSup', self.gf('django.db.models.fields.IntegerField')()),
            ('RangoInf', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'principal', ['Tipo_marcacion'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'principal_userprofile')

        # Deleting model 'Vinculacion'
        db.delete_table(u'principal_vinculacion')

        # Deleting model 'Proposito'
        db.delete_table(u'principal_proposito')

        # Deleting model 'Marcacion'
        db.delete_table(u'principal_marcacion')

        # Deleting model 'Tipo_marcacion'
        db.delete_table(u'principal_tipo_marcacion')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'principal.marcacion': {
            'Meta': {'object_name': 'Marcacion'},
            'cumplimiento': ('django.db.models.fields.IntegerField', [], {}),
            'dia': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proposito': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Proposito']"})
        },
        u'principal.proposito': {
            'Meta': {'object_name': 'Proposito'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes_ano': ('django.db.models.fields.DateField', [], {}),
            'proposito': ('django.db.models.fields.TextField', [], {}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'vinculacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Vinculacion']"})
        },
        u'principal.tipo_marcacion': {
            'Meta': {'object_name': 'Tipo_marcacion'},
            'RangoInf': ('django.db.models.fields.IntegerField', [], {}),
            'RangoSup': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'principal.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contrato_pedagogico': ('django.db.models.fields.TextField', [], {}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'grupo_de_vida': ('django.db.models.fields.TextField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideal_personal': ('django.db.models.fields.TextField', [], {}),
            'pais': ('django.db.models.fields.TextField', [], {'max_length': '50'}),
            'sexo': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'principal.vinculacion': {
            'Meta': {'object_name': 'Vinculacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'vinculacion': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['principal']