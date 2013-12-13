# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campaign'
        db.create_table(u'lead_center_campaign', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('view', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'lead_center', ['Campaign'])

        # Adding model 'Lead'
        db.create_table(u'lead_center_lead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lead_center.Campaign'])),
            ('phone', self.gf('django.db.models.fields.IntegerField')(max_length=15)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('agent', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
        ))
        db.send_create_signal(u'lead_center', ['Lead'])


    def backwards(self, orm):
        # Deleting model 'Campaign'
        db.delete_table(u'lead_center_campaign')

        # Deleting model 'Lead'
        db.delete_table(u'lead_center_lead')


    models = {
        u'lead_center.campaign': {
            'Meta': {'object_name': 'Campaign'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'view': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'lead_center.lead': {
            'Meta': {'object_name': 'Lead'},
            'agent': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lead_center.Campaign']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.IntegerField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['lead_center']