# _*_ coding: utf-8 _*_

from django.apps import AppConfig


class StudentsAppConfig(AppConfig):
    name = 'students'
    verbose_name = u'База студентів'

    def ready(self):
    	from students import signals
