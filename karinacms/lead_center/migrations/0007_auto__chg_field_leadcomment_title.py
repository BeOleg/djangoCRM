# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'LeadComment.title'
        db.alter_column(u'lead_center_leadcomment', 'title', self.gf('django.db.models.fields.CharField')(max_length=512))

    def backwards(self, orm):

        # Changing field 'LeadComment.title'
        db.alter_column(u'lead_center_leadcomment', 'title', self.gf('django.db.models.fields.TextField')(max_length=512))

    models = {
        u'lead_center.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'view': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'lead_center.lead': {
            'Meta': {'object_name': 'Lead'},
            'agent': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lead_center.Campaign']"}),
            'campaign_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'lead_center.leadcomment': {
            'Meta': {'object_name': 'LeadComment'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lead': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lead_center.Lead']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['lead_center']