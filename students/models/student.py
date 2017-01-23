from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class Student(models.Model):
  #Student Model
  class Meta(object):
    verbose_name = _(u"Student")
    verbose_name_plural = _(u"Students")
  first_name = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"first_name"))
  last_name = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"last_name"))
  middle_name = models.CharField(
    max_length=256,
    blank=True,
    verbose_name=_(u"surname"),
    default='')
  birthday = models.DateField(
    blank=False,
    verbose_name=_(u"birthday"),
    null=True)
  photo = models.ImageField(
    blank=True,
    verbose_name=_(u"photo"),
    null=True)
  ticket = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=_(u"ticket"))
  student_group_id = models.ForeignKey('Group',
    verbose_name=_(u"group"),
    blank=False,
    null=True,
    on_delete=models.PROTECT)
  notes = models.TextField(
    blank=True,
    verbose_name=_(u"Additional notes"))
  
  def __unicode__(self):
    return u"%s %s" % (self.first_name, self.last_name)
