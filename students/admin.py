# -*- coding: utf-8 -*-
from django.contrib import admin
from .models.student import Student
from .models.group import Group
from .models.exam import Exam
from .models.monthjournal import MonthJournal
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError
from correct_admin import *





admin.site.register(Student,StudentAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(MonthJournal)


