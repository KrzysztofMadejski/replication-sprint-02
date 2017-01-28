# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Party'
        db.create_table(u'crowdataapp_party', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='128')),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length='128')),
            ('parldata_id', self.gf('django.db.models.fields.CharField')(max_length='64')),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'crowdataapp', ['Party'])

        # Adding model 'Politician'
        db.create_table(u'crowdataapp_politician', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='128')),
            ('parliamentary_id', self.gf('django.db.models.fields.CharField')(max_length='24')),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length='256')),
            ('party', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='members', null=True, to=orm['crowdataapp.Party'])),
            ('parldata_id', self.gf('django.db.models.fields.CharField')(max_length='64')),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'crowdataapp', ['Politician'])

        # Adding field 'Document.politician'
        db.add_column(u'crowdataapp_document', 'politician',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='declarations', null=True, to=orm['crowdataapp.Politician']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Party'
        db.delete_table(u'crowdataapp_party')

        # Deleting model 'Politician'
        db.delete_table(u'crowdataapp_politician')

        # Deleting field 'Document.politician'
        db.delete_column(u'crowdataapp_document', 'politician_id')


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
        u'crowdataapp.canonicalfieldentrylabel': {
            'Meta': {'object_name': 'CanonicalFieldEntryLabel'},
            'document_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'canonical_values'", 'null': 'True', 'to': u"orm['crowdataapp.DocumentSet']"}),
            'form_field': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'form_field'", 'to': u"orm['crowdataapp.DocumentSetFormField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'})
        },
        u'crowdataapp.document': {
            'Meta': {'object_name': 'Document'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents'", 'to': u"orm['crowdataapp.DocumentSet']"}),
            'entries_threshold_override': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'opened_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'politician': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'declarations'", 'null': 'True', 'to': u"orm['crowdataapp.Politician']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': "'512'"}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'crowdataapp.documentset': {
            'Meta': {'object_name': 'DocumentSet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'entries_threshold': ('django.db.models.fields.IntegerField', [], {'default': '3'}),
            'head_html': ('django.db.models.fields.TextField', [], {'default': '\'<!-- <script> or <link rel="stylesheet"> tags go here -->\'', 'null': 'True'}),
            'header_image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'populate_from': "'name'", 'overwrite': 'False'}),
            'tosum_field': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tosum_fields'", 'null': 'True', 'to': u"orm['crowdataapp.DocumentSetFormField']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'crowdataapp.documentsetfieldentry': {
            'Meta': {'object_name': 'DocumentSetFieldEntry'},
            'canonical_label': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'null': 'True', 'to': u"orm['crowdataapp.CanonicalFieldEntryLabel']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': u"orm['crowdataapp.DocumentSetFormEntry']"}),
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crowdataapp.DocumentSetFormField']"}),
            'field_id': ('django.db.models.fields.IntegerField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'crowdataapp.documentsetform': {
            'Meta': {'object_name': 'DocumentSetForm'},
            'button_text': ('django.db.models.fields.CharField', [], {'default': "u'Submit'", 'max_length': '50'}),
            'document_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'form'", 'unique': 'True', 'to': u"orm['crowdataapp.DocumentSet']"}),
            'email_copies': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email_from': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'email_message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email_subject': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'response': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'send_email': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'crowdataapp.documentsetformentry': {
            'Meta': {'object_name': 'DocumentSetFormEntry'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'form_entries'", 'null': 'True', 'to': u"orm['crowdataapp.Document']"}),
            'entry_time': ('django.db.models.fields.DateTimeField', [], {}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['crowdataapp.DocumentSetForm']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'crowdataapp.documentsetformfield': {
            'Meta': {'object_name': 'DocumentSetFormField'},
            'autocomplete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'choices': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'default': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'blank': 'True'}),
            'field_type': ('django.db.models.fields.IntegerField', [], {}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fields'", 'to': u"orm['crowdataapp.DocumentSetForm']"}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help_text': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'placeholder_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'verify': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'crowdataapp.documentsetrankingdefinition': {
            'Meta': {'object_name': 'DocumentSetRankingDefinition'},
            'amount_rows_on_home': ('django.db.models.fields.IntegerField', [], {'default': '10', 'null': 'True'}),
            'document_set': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rankings'", 'to': u"orm['crowdataapp.DocumentSet']"}),
            'grouping_function': ('django.db.models.fields.CharField', [], {'default': "'SUM'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label_field': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'label_fields'", 'to': u"orm['crowdataapp.DocumentSetFormField']"}),
            'magnitude_field': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'magnitude_fields'", 'null': 'True', 'to': u"orm['crowdataapp.DocumentSetFormField']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'sort_order': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'crowdataapp.feedback': {
            'Meta': {'object_name': 'Feedback'},
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crowdataapp.Document']"}),
            'feedback_text': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'crowdataapp.party': {
            'Meta': {'object_name': 'Party'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'parldata_id': ('django.db.models.fields.CharField', [], {'max_length': "'64'"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'crowdataapp.politician': {
            'Meta': {'object_name': 'Politician'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': "'256'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'parldata_id': ('django.db.models.fields.CharField', [], {'max_length': "'64'"}),
            'parliamentary_id': ('django.db.models.fields.CharField', [], {'max_length': "'24'"}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'members'", 'null': 'True', 'to': u"orm['crowdataapp.Party']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'crowdataapp.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'country': ('django_countries.fields.CountryField', [], {'max_length': '2', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'show_in_leaderboard': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['crowdataapp']