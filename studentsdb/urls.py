"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include,url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from students.view.journal import JournalView
from students.view.exams import ExamList,ExamCreate, ExamUpdate, ExamDelete
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView, TemplateView
from students.view.student import stud_add, student_edit, student_delete
from students.view.group import groups_add, groups_edit, groups_delete 
from students.view.logs import logs
from students.view.contact_admin import contact_admin
from django.contrib.auth.decorators import login_required
from registration.backends.default import views as registration_views
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy
from registration.backends.default.views import RegistrationView




js_info_dict = {
'packages': ('students',),
}

urlpatterns = patterns('',
# Students urls
url(r'^$', 'students.view.student.students_list', name='main'),
url(r'^stud_add$', login_required(stud_add), name='s_add'),
url(r'^students/(?P<pk>\d+)/edit/$',login_required(student_edit),
name='students_edit'),
url(r'^students/(?P<pk>\d+)/delete/$',login_required(student_delete),name='students_delete'),
#journal
url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
#Groups urls
url(r'^grup$', 'students.view.groups.grup', name='groups'),
url(r'^groups_add$', 'students.view.group.groups_add', name='groups_add'),
url(r'^groups/(?P<pk>\d+)/edit/$',
'students.view.group.groups_edit', name='groups_edit'),
url(r'^groups/(?P<pk>\d+)/delete/$',
'students.view.group.groups_delete', name='groups_delete'),
url(r'^groups/(?P<pk>\d+)/one/$',
'students.view.group.groups_one', name='groups_one'),
url(r'^admin/', include(admin.site.urls)),
#exams url
url(r'^exams$', ExamList.as_view(), name='exams'),
url(r'^exam_add$', login_required(ExamCreate.as_view()), name='exam_add'),
url(r'^exams/(?P<pk>\d+)/edit/$', login_required(ExamUpdate.as_view()), name='exam_edit'),
url(r'^exams/(?P<pk>\d+)/delete/$', login_required(ExamDelete.as_view()), name='exam_delete'),
#logs
url(r'^logs$', login_required(logs), name='logs'),
# Contact Admin Form
url(r'^contact-admin/$', login_required(contact_admin),
name='contact_admin'),
#i18n of js
url(r'^jsi18n.js$', 'django.views.i18n.javascript_catalog', js_info_dict),

# User Related urls
url(r'^users/profile/$', login_required(TemplateView.as_view(
template_name='registration/profile.html')), name='profile'),
url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'main'}, name='auth_logout'),
url(r'^register/complete/$', TemplateView.as_view(template_name='registration/confirm_email.html'), name='registration_complete'),
url(r'^users/', include('registration.backends.default.urls', namespace='users')),
url(r'^users/login/', include('registration.auth_urls', namespace='logins')),
url(r'^users/activate/(?P<activation_key>\w+)/$', registration_views.ActivationView.as_view(),
name='registration_activate'),
url(r'^users/activate/complete/$',
TemplateView.as_view(template_name='registration/activation_complete.html'),
name='registration_activation_complete'),
url(r'^password/reset/$',
                           auth_views.password_reset,
                           {'post_reset_redirect': reverse_lazy('auth_password_reset_done')},
                           name='auth_password_reset'),
url(r'^password/reset/done/$',
                           auth_views.password_reset_done,
                           name='auth_password_reset_done'),
url(r'^register/$',
            RegistrationView.as_view(),
            name='registration_register'),

# Social Auth Related urls
url('^social/', include('social.apps.django_app.urls', namespace ='social')),
)

if DEBUG:
 # serve files from media folder
 urlpatterns += patterns('',
 url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
 'document_root': MEDIA_ROOT}))
