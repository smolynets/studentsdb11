from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class StudentsAppConfig(AppConfig):
    name = 'students'
    verbose_name = _(u'Students base')

    def ready(self):
    	from students import signals
