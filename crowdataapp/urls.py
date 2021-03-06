from django.conf.urls import patterns, url
from crowdataapp import views

urlpatterns = patterns('crowdataapp.views',
                       url(r'^$',
                          'document_set_index',
                          name='document_set_index'),
                       url(r'^pleaselogin$',
                           'login',
                           name='login_page'),
                       url(r'^anonymouselogin$',
                           'login_anonymously',
                           name='login_anonymously'),
                       url(r'^feedback/(?P<document_id>[\w-]+)$',
                           'feedback',
                           name='feedback'),
                       url(r'^logout$',
                           'logout',
                           name='logout_page'),
                       url(r'^afterlogin$',
                           'after_login',
                           name='after_login'),
                       url(r'^profile$',
                           'edit_profile',
                           name='edit_profile'),
                       url(r'^(?P<document_set>[\w-]+)$',
                           'document_set_view',
                           name='document_set_view'),
                       url(r'^(?P<document_set>[\w-]+)/new_transcription$',
                           'transcription_new',
                           name='new_transcription'),
                       url(r'^(?P<document_set>[\w-]+)/new_transcription/(?P<filename>[\w-]+)$',
                           'transcription_new',
                           name='new_transcription'),
                       url(r'^(?P<document_set>[\w-]+)/new_transcription_by_cat/(?P<category>[\w-]+)$',
                           'transcription_new',
                           name='new_transcription_by_cat'),
                       url(r'^(?P<document_set>[\w-]+)/(?P<document_id>[\w-]+)$',
                           'show_document',
                           name='show_document'),
                       url(r'^(?P<document_set>[\w-]+)/autocomplete/(?P<field_name>[\w-]+)$',
                           'autocomplete_field',
                           name='autocomplete_field'),
                       url(r'crowdata/form/(?P<slug>[\w-]+)',
                           'form_detail',
                           name='crowdata_form_detail'),
                       url(r'^(?P<document_set>[\w-]+)/ranking/(?P<ranking_id>[\w-]+)$',
                           'ranking_all',
                           name='ranking_all'),
                       url(r'^(?P<document_set>[\w-]+)/users/(?P<username>[\w-]+)$',
                           'user_profile',
                           name='user_profile'),
                       url(r'^(?P<document_set>[\w-]+)/all/users$',
                           'users_all',
                           name='users_all'),
                       url(r'^(?P<document_set>[\w-]+)/(?P<field_id>[\w-]+)/(?P<canon_id>[\w-]+)$',
                           'documents_by_entry_value',
                           name='documents_by_entry_value'),
                       url('^(?P<document_set_id>[\w-]+)/answers/$',
                                  'answers_view',
                                  name="document_set_answers_csv"),
)
