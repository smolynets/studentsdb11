# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
class Group(models.Model):
  """Group Model"""
  class Meta(object):
    verbose_name = _(u"group")
    verbose_name_plural = _(u"groups")
  title = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=u"Назва")
  leader = models.OneToOneField('Student',
    verbose_name=u"Староста",
    blank=True,
    null=True,
    on_delete=models.SET_NULL)
  notes = models.TextField(
    blank=True,
    verbose_name=u"Додаткові нотатки")
  def __unicode__(self):
    return u"%s" % (self.title,)
