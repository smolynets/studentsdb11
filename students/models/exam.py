from django.utils.translation import ugettext_lazy as _
from django.db import models
class Exam(models.Model):
  """Exam Model"""
  class Meta(object):
    verbose_name = _(u"Exam")
    verbose_name_plural = _(u"Exams")
  title = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"name"))
  group = models.ForeignKey('Group',
    verbose_name=_(u'Group'),
    blank=False,
    null=True,)

  date = models.DateField(
    blank=True,
    verbose_name=_(u"dates"))
  def __unicode__(self):
    return u"%s %s" % (self.title, self.group)








