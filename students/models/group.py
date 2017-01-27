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
    verbose_name=_(u"name"))
  leader = models.OneToOneField('Student',
    verbose_name=_(u"leader"),
    blank=True,
    null=True,
    on_delete=models.SET_NULL)
  notes = models.TextField(
    blank=True,
    verbose_name=_(u"Additional notes"))
  def __unicode__(self):
    return u"%s" % (self.title,)
