# -*- coding: utf-8 -*-
from django.db import models
class MonthJournal(models.Model):
  
    class Meta:
      verbose_name = u'Місячний Журнал'
      verbose_name_plural = u'Місячні Журнали'
      
    student = models.ForeignKey('Student',
      verbose_name=u'Студент',
      blank=False,
      unique_for_month='date')
    date = models.DateField(
      verbose_name=u'Дата',
      blank=False)
    local_vars = locals()
    for num in range(1, 32):
      local_vars.update({'present_day'+str(num) : models.BooleanField(default=False)})
   
    def __unicode__(self):
      return u'%s: %d, %d' % (self.student.last_name, self.date.month,
        self.date.year)


class logentry(models.Model):
  level = models.CharField(
    max_length=20,
    blank=False)
  asctime = models.DateTimeField(
    blank=False,
    null=True)
  module = models.CharField(
    max_length=100,
    blank=False,)
  message = models.TextField(
    blank=False,)
  def __unicode__(self):
    return u"%s %s %s %s" % (self.level, self.asctime, self.module, self.message)











